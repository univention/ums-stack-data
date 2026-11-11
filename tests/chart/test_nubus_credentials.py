# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2026 Univention GmbH

from pytest_helm.utils import load_yaml

# The name and key predate this chart; the Secret moved here from the nubus umbrella chart.
CREDENTIALS = "release-name-nubus-credentials"
ADMINISTRATOR = "release-name-stack-data-ums-administrator"


def test_credentials_hold_the_administrator_password(chart):
    values = load_yaml("templateContext:\n  initialPasswordAdministrator: stub-password\n")

    result = chart.helm_template(values)

    credentials = result.get_resource(kind="Secret", name=CREDENTIALS)
    assert credentials["stringData"] == {"administrator_password": "stub-password"}


def test_credentials_hold_the_generated_administrator_password(chart):
    values = load_yaml("templateContext:\n  initialPasswordAdministrator: null\n")

    result = chart.helm_template(values)

    generated = result.get_resource(kind="Secret", name=ADMINISTRATOR)["stringData"]["password"]
    assert generated
    assert result.get_resource(kind="Secret", name=CREDENTIALS)["stringData"]["administrator_password"] == generated


def test_no_credentials_for_a_referenced_administrator_password(chart):
    values = load_yaml(
        """
        templateContext:
          initialPasswordAdministrator:
            kubernetesSecret:
              name: operator-secret
              key: administrator-password
        """,
    )

    result = chart.helm_template(values)

    assert [s for s in result.get_resources(kind="Secret") if s["metadata"]["name"] == CREDENTIALS] == []
