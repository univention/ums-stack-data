# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2026 Univention GmbH

import base64

import pytest

from univention.data_loader.secret_refs import KubernetesSecretReader


class StubResponse:
    def __init__(self, status_code: int, body: dict | None = None):
        self.status_code = status_code
        self.body = body or {}

    def json(self):
        return self.body


class StubSession:
    """Answers GET requests from a dict of URL to response and records each call."""

    def __init__(self, responses: dict[str, StubResponse]):
        self.responses = responses
        self.calls = []

    def get(self, url, **kwargs):
        self.calls.append((url, kwargs))
        return self.responses.get(url, StubResponse(404))


API = "https://10.0.0.1:443"
SECRETS_URL = f"{API}/api/v1/namespaces/stub-namespace/secrets"


def secret(data: dict[str, bytes]) -> StubResponse:
    return StubResponse(200, {"data": {key: base64.b64encode(value).decode() for key, value in data.items()}})


@pytest.fixture
def service_account_dir(tmp_path, monkeypatch):
    (tmp_path / "token").write_text("stub-token")
    (tmp_path / "namespace").write_text("stub-namespace")
    (tmp_path / "ca.crt").write_text("stub-ca")
    monkeypatch.setenv("KUBERNETES_SERVICE_HOST", "10.0.0.1")
    monkeypatch.setenv("KUBERNETES_SERVICE_PORT", "443")
    return tmp_path


def test_reads_a_key_from_a_secret_in_its_own_namespace(service_account_dir):
    session = StubSession({f"{SECRETS_URL}/admin": secret({"password": b"s3cr3t\n"})})
    reader = KubernetesSecretReader(service_account_dir, session=session)

    assert reader.get("admin", "password") == "s3cr3t\n"
    [(url, kwargs)] = session.calls
    assert kwargs["headers"] == {"Authorization": "Bearer stub-token"}
    assert kwargs["verify"] == str(service_account_dir / "ca.crt")


def test_reads_each_secret_only_once(service_account_dir):
    session = StubSession({f"{SECRETS_URL}/ldapsearch": secret({"ox": b"a", "keycloak": b"b"})})
    reader = KubernetesSecretReader(service_account_dir, session=session)

    assert [reader.get("ldapsearch", "ox"), reader.get("ldapsearch", "keycloak")] == ["a", "b"]
    assert len(session.calls) == 1


@pytest.mark.parametrize(
    ("response", "message"),
    [
        pytest.param(StubResponse(404), "Secret admin not found in namespace stub-namespace", id="not found"),
        pytest.param(StubResponse(403), "Access to Secret admin in namespace stub-namespace denied", id="forbidden"),
        pytest.param(secret({"other": b"leak-me"}), "Secret admin has no key password", id="missing key"),
        pytest.param(secret({"password": b"\xffleak-me"}), "Secret admin key password is not UTF-8", id="not utf-8"),
    ],
)
def test_a_failed_read_names_the_secret_and_hides_its_data(service_account_dir, response, message):
    from univention.data_loader.secret_refs import SecretReadError

    reader = KubernetesSecretReader(service_account_dir, session=StubSession({f"{SECRETS_URL}/admin": response}))

    with pytest.raises(SecretReadError) as error:
        reader.get("admin", "password")

    assert message in str(error.value)
    assert "leak-me" not in str(error.value)
    assert error.value.__cause__ is None or "leak-me" not in str(error.value.__cause__)
