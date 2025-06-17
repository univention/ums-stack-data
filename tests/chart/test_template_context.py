# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2024-2025 Univention GmbH

from pytest_helm.utils import load_yaml


def test_user_adds_value(chart):
    values = load_yaml(
        """
        templateContext:
          stubName: "stub-value"
        """,
    )
    result = chart.helm_template(values)
    context_secret = result.get_resource(name="release-name-stack-data-ums-context")
    context_data = _get_template_context_data(context_secret)
    assert context_data["stubName"] == "stub-value"


def test_user_overrides_value(chart):
    values = load_yaml(
        """
        templateContext:
          ldapBaseDn: "dc=testsuite,dc=test"
        """,
    )
    result = chart.helm_template(values)
    context_secret = result.get_resource(name="release-name-stack-data-ums-context")
    context_data = _get_template_context_data(context_secret)
    assert context_data["ldapBaseDn"] == "dc=testsuite,dc=test"


def _get_template_context_data(context_secret):
    context_yaml = context_secret["stringData"]["context.yaml"]
    context_data = load_yaml(context_yaml)
    return context_data
