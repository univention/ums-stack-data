# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2026 Univention GmbH

import pytest

from univention.data_loader.secret_refs import InvalidReference, SecretReadError, resolve_references


class FakeSecretReader:
    def __init__(self, secrets: dict[tuple[str, str], str]):
        self.secrets = secrets

    def get(self, name: str, key: str) -> str:
        if (name, key) not in self.secrets:
            raise SecretReadError(f"Secret {name} has no key {key}")
        return self.secrets[(name, key)]


def ref(name: str, key: str) -> dict:
    return {"kubernetesSecret": {"name": name, "key": key}}


def test_replaces_a_top_level_reference_with_the_secret_value():
    reader = FakeSecretReader({("admin", "password"): "stub-secret"})
    context = {"initialPasswordAdministrator": ref("admin", "password"), "domainName": "example.org"}

    result = resolve_references(context, reader)

    assert result == {"initialPasswordAdministrator": "stub-secret", "domainName": "example.org"}


def test_replaces_references_in_list_items():
    reader = FakeSecretReader({("ldapsearch-ox", "password"): "ox-secret"})
    context = {"ldapSearchUsers": [{"name": "ldapsearch_ox", "password": ref("ldapsearch-ox", "password")}]}

    result = resolve_references(context, reader)

    assert result == {"ldapSearchUsers": [{"name": "ldapsearch_ox", "password": "ox-secret"}]}


@pytest.mark.parametrize(
    "malformed",
    [
        pytest.param({"kubernetesSecret": {"name": "admin", "key": "password"}, "extra": 1}, id="sibling key"),
        pytest.param({"kubernetesSecret": {"name": "admin"}}, id="missing key"),
        pytest.param({"kubernetesSecret": {"key": "password"}}, id="missing name"),
        pytest.param({"kubernetesSecret": {"name": "", "key": "password"}}, id="empty name"),
        pytest.param({"kubernetesSecret": {"name": "admin", "key": 1}}, id="key not a string"),
        pytest.param({"kubernetesSecret": {"name": "a", "key": "b", "namespace": "c"}}, id="unknown field"),
        pytest.param({"kubernetesSecret": "admin"}, id="not a mapping"),
    ],
)
def test_rejects_a_malformed_reference_and_names_its_path(malformed):
    context = {"ldapSearchUsers": [{"password": malformed}]}

    with pytest.raises(InvalidReference, match=r"ldapSearchUsers\[0\]\.password"):
        resolve_references(context, FakeSecretReader({}))


def test_a_failed_read_names_the_context_path():
    context = {"svc": {"password": ref("svc-portal-server", "password")}}

    with pytest.raises(SecretReadError, match=r"^svc\.password: Secret svc-portal-server has no key password$"):
        resolve_references(context, FakeSecretReader({}))
