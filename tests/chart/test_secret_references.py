# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2026 Univention GmbH

import pytest
from pytest_helm.utils import load_yaml

CONTEXT_SECRET = "release-name-stack-data-ums-context"

built_in_passwords = pytest.mark.parametrize(
    ("context_key", "user_secret"),
    [
        ("initialPasswordAdministrator", "release-name-stack-data-ums-administrator"),
        ("svcPortalServerUserPassword", "release-name-stack-data-ums-svc-portal-server"),
        ("readonlyUserPassword", "release-name-stack-data-ums-readonly-user"),
    ],
)


def ref(name, key):
    return {"kubernetes_secret": {"name": name, "key": key}}


def context_of(result):
    return load_yaml(result.get_resource(name=CONTEXT_SECRET)["stringData"]["context.yaml"])


@built_in_passwords
def test_a_given_password_is_referenced_from_its_user_secret(chart, context_key, user_secret):
    values = load_yaml(f"templateContext:\n  {context_key}: stub-password\n")

    result = chart.helm_template(values)

    assert context_of(result)[context_key] == ref(user_secret, "password")
    assert result.get_resource(kind="Secret", name=user_secret)["stringData"]["password"] == "stub-password"


@built_in_passwords
def test_a_referenced_password_is_kept_and_has_no_user_secret(chart, context_key, user_secret):
    values = load_yaml(
        f"""
        templateContext:
          {context_key}:
            kubernetes_secret:
              name: operator-secret
              key: operator-key
        """,
    )

    result = chart.helm_template(values)

    assert context_of(result)[context_key] == ref("operator-secret", "operator-key")
    assert [s for s in result.get_resources(kind="Secret") if s["metadata"]["name"] == user_secret] == []


def test_the_service_account_may_read_secrets_in_its_namespace(chart):
    result = chart.helm_template()

    role = result.get_resource(kind="Role", name="release-name-stack-data-ums")
    assert role["rules"] == [{"apiGroups": [""], "resources": ["secrets"], "verbs": ["get"]}]
    binding = result.get_resource(kind="RoleBinding", name="release-name-stack-data-ums")
    assert binding["roleRef"] == {
        "apiGroup": "rbac.authorization.k8s.io",
        "kind": "Role",
        "name": role["metadata"]["name"],
    }
    assert binding["subjects"] == [
        {"kind": "ServiceAccount", "name": "release-name-stack-data-ums", "namespace": role["metadata"]["namespace"]},
    ]


def test_the_job_pod_mounts_the_service_account_token(chart):
    result = chart.helm_template()

    [job] = result.get_resources(kind="Job")
    assert job["spec"]["template"]["spec"]["automountServiceAccountToken"] is True
