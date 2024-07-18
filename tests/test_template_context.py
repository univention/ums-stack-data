# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2024 Univention GmbH

from yaml import safe_load


def test_user_adds_value(helm, chart_path):
    values = safe_load(
        """
        templateContext:
          stubName: "stub-value"
        """,
    )
    result = helm.helm_template(chart_path, values)
    context_secret = helm.get_resource(
        result,
        name="release-name-stack-data-ums-context",
    )
    context_data = _get_template_context_data(context_secret)
    assert context_data["stubName"] == "stub-value"


def test_user_overrides_value(helm, chart_path):
    values = safe_load(
        """
        templateContext:
          ldapBaseDn: "dc=testsuite,dc=test"
        """,
    )
    result = helm.helm_template(chart_path, values)
    context_secret = helm.get_resource(
        result,
        name="release-name-stack-data-ums-context",
    )
    context_data = _get_template_context_data(context_secret)
    assert context_data["ldapBaseDn"] == "dc=testsuite,dc=test"


def test_install_umc_policies_is_bool_by_default(helm, chart_path):
    result = helm.helm_template(chart_path)
    context_secret = helm.get_resource(
        result,
        name="release-name-stack-data-ums-context",
    )
    context_data = _get_template_context_data(context_secret)
    assert type(context_data["installUmcPolicies"]) == bool


def _get_template_context_data(context_secret):
    context_yaml = context_secret["stringData"]["context.yaml"]
    context_data = safe_load(context_yaml)
    return context_data
