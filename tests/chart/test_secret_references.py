# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2026 Univention GmbH

import subprocess

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
    return {"kubernetesSecret": {"name": name, "key": key}}


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
            kubernetesSecret:
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


SERVICE_ACCOUNT_DIR = "/var/run/secrets/kubernetes.io/serviceaccount"


def pod_spec(result):
    [job] = result.get_resources(kind="Job")
    return job["spec"]["template"]["spec"]


def test_only_the_main_container_gets_the_service_account_token(chart):
    spec = pod_spec(chart.helm_template())

    assert spec["automountServiceAccountToken"] is False
    [volume] = [v for v in spec["volumes"] if v["name"] == "service-account-token"]
    assert [next(iter(source)) for source in volume["projected"]["sources"]] == [
        "serviceAccountToken",
        "configMap",
        "downwardAPI",
    ]
    [main] = spec["containers"]
    assert {"name": "service-account-token", "mountPath": SERVICE_ACCOUNT_DIR, "readOnly": True} in main["volumeMounts"]
    for init in spec["initContainers"]:
        assert "service-account-token" not in [m["name"] for m in init.get("volumeMounts", [])]


def test_an_existing_service_account_gets_the_role(chart):
    values = load_yaml(
        """
        serviceAccount:
          create: false
          name: operator-account
        """,
    )

    result = chart.helm_template(values)

    assert pod_spec(result)["serviceAccountName"] == "operator-account"
    assert result.get_resources(kind="ServiceAccount") == []
    binding = result.get_resource(kind="RoleBinding", name="release-name-stack-data-ums")
    assert [s["name"] for s in binding["subjects"]] == ["operator-account"]


def test_an_existing_service_account_needs_a_name(chart):
    values = load_yaml("serviceAccount:\n  create: false\n")

    with pytest.raises(subprocess.CalledProcessError) as error:
        chart.helm_template(values)

    assert "serviceAccount.name" in error.value.stderr


def test_rbac_can_be_disabled(chart):
    values = load_yaml("rbac:\n  create: false\n")

    result = chart.helm_template(values)

    assert result.get_resources(kind="Role") == []
    assert result.get_resources(kind="RoleBinding") == []
    assert pod_spec(result)["serviceAccountName"] == "release-name-stack-data-ums"
