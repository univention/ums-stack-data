# SPDX-FileCopyrightText: 2024-2025 Univention GmbH
# SPDX-License-Identifier: AGPL-3.0-only

import os.path

import pytest


@pytest.fixture
def helm_values(request):
    """
    By default use "helm/stack-data-ums/linter_values.yaml".
    """
    default_values = ["helm/stack-data-ums/linter_values.yaml"]
    return request.config.option.values or default_values


@pytest.fixture
def chart_path(pytestconfig):
    """
    Path to the Helm chart which shall be tested.
    """
    chart_path = pytestconfig.option.chart_path
    if not chart_path:
        tests_path = os.path.dirname(os.path.abspath(__file__))
        chart_path = os.path.normpath(
            os.path.join(tests_path, "../../helm/stack-data-ums"),
        )
    return chart_path
