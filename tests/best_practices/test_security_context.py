# SPDX-FileCopyrightText: 2024 Univention GmbH
# SPDX-License-Identifier: AGPL-3.0-only

# Ruff has problems with multiline f-strings
# ruff: noqa: F541

import pytest
from yaml import safe_load


def test_pod_security_context_can_be_disabled(helm, chart_path):
    values = safe_load(
        """
        podSecurityContext:
          enabled: false
          fsGroup: 1000
          fsGroupChangePolicy: "Always"
        """,
    )
    result = helm.helm_template(chart_path, values)
    manifest = helm.get_resource(result, kind="Job")
    pod_security_context = manifest["spec"]["template"]["spec"].get("securityContext", {})
    expected_security_context = {}
    assert pod_security_context == expected_security_context


def test_pod_security_context_can_be_specified(helm, chart_path):
    values = safe_load(
        """
        podSecurityContext:
          enabled: true
          fsGroup: 1000
          fsGroupChangePolicy: "Always"
        """,
    )
    result = helm.helm_template(chart_path, values)
    manifest = helm.get_resource(result, kind="Job")
    pod_security_context = manifest["spec"]["template"]["spec"]["securityContext"]
    expected_security_context = {
        "fsGroup": 1000,
        "fsGroupChangePolicy": "Always",
    }
    assert pod_security_context == expected_security_context
