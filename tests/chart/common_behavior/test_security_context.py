# SPDX-FileCopyrightText: 2024-2025 Univention GmbH
# SPDX-License-Identifier: AGPL-3.0-only

# Ruff has problems with multiline f-strings
# ruff: noqa: F541

from pytest_helm.utils import get_containers, load_yaml


def test_pod_security_context_can_be_disabled(chart):
    values = load_yaml(
        """
        podSecurityContext:
          enabled: false
          fsGroup: 1000
          fsGroupChangePolicy: "Always"
        """,
    )
    result = chart.helm_template(values)
    manifest = result.get_resource(kind="Job")
    pod_security_context = manifest.findone(
        "spec.template.spec.securityContext",
        default={},
    )
    expected_security_context = {}
    assert pod_security_context == expected_security_context


def test_pod_security_context_is_applied(chart):
    values = load_yaml(
        """
        podSecurityContext:
          enabled: true
          fsGroup: 1000
          fsGroupChangePolicy: "Always"
        """,
    )
    result = chart.helm_template(values)
    manifest = result.get_resource(kind="Job")
    pod_security_context = manifest.findone("spec.template.spec.securityContext")
    expected_security_context = {
        "fsGroup": 1000,
        "fsGroupChangePolicy": "Always",
    }
    assert pod_security_context == expected_security_context


def test_container_security_context_can_be_disabled(chart):
    values = load_yaml(
        """
        containerSecurityContext:
          enabled: false
          capabilities:
            drop: []
          runAsUser: 9876
        """,
    )
    expected_security_context = {}
    result = chart.helm_template(values)
    _assert_all_have_security_context(result, expected_security_context)


def test_container_security_context_is_applied(chart):
    values = load_yaml(
        """
        containerSecurityContext:
          enabled: true
          capabilities:
            drop: []
          runAsUser: 9876
        """,
    )
    expected_security_context = {
        "capabilities": {
            "drop": [],
        },
        "runAsUser": 9876,
    }

    result = chart.helm_template(values)
    _assert_all_have_security_context(result, expected_security_context)


def _assert_all_have_security_context(result, expected_security_context):
    job = result.get_resource(kind="Job")
    containers = get_containers(job)
    for container in containers:
        security_context = container.get("securityContext", {})
        name = container["name"]
        assert security_context.items() >= expected_security_context.items(), (
            f'Wrong securityContext in container "{name}"'
        )
