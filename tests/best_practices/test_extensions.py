# SPDX-FileCopyrightText: 2024 Univention GmbH
# SPDX-License-Identifier: AGPL-3.0-only

# Ruff has problems with multiline f-strings
# ruff: noqa: F541

from yaml import safe_load

from utils import findall


def test_no_extensions_by_default(helm, chart_path):
    result = helm.helm_template(chart_path)
    extensions = _get_extensions_of_job(helm, result)
    assert extensions == []


def _get_extensions_of_job(helm, result):
    manifest = helm.get_resource(result, kind="Job")
    init_containers = findall(manifest, "spec.template.spec.initContainers")
    extensions = [c for c in init_containers if c["name"].endswith("-extension")]
    return extensions
