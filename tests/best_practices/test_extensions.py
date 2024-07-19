# SPDX-FileCopyrightText: 2024 Univention GmbH
# SPDX-License-Identifier: AGPL-3.0-only

# Ruff has problems with multiline f-strings
# ruff: noqa: F541

import pytest
from yaml import safe_load

from utils import findall


@pytest.fixture
def stub_extension():
    """
    Return a stub extension configuration with all values set to stub values.
    """
    values = safe_load(
        """
        name: "stub-test"
        image:
          registry: "stub-registry"
          repository: "stub-repository"
          imagePullPolicy: "stub-image-pull-policy"
          tag: "stub-tag"
        """,
    )
    return values


def test_no_extensions_by_default(helm, chart_path):
    result = helm.helm_template(chart_path)
    extensions = _get_extensions_of_job(helm, result)
    assert extensions == []


@pytest.mark.parametrize("key", ["extensions", "systemExtensions"])
def test_extension_configured(helm, chart_path, key, stub_extension):
    values = {
        key: [stub_extension],
    }

    result = helm.helm_template(chart_path, values)
    extensions = _get_extensions_of_job(helm, result)
    assert len(extensions) == 1

    extension = extensions[0]
    assert extension["name"] == "load-stub-test-extension"


@pytest.mark.parametrize("key", ["extensions", "systemExtensions"])
def test_extension_image(helm, chart_path, key, stub_extension):
    values = {
        key: [stub_extension],
    }
    result = helm.helm_template(chart_path, values)
    extensions = _get_extensions_of_job(helm, result)
    extension = extensions[0]
    assert extension["image"] == "stub-registry/stub-repository:stub-tag"


@pytest.mark.parametrize("key", ["extensions", "systemExtensions"])
def test_extension_image_with_global_registry(helm, chart_path, key, stub_extension):
    del stub_extension["image"]["registry"]
    values = {
        "global": {
            "imageRegistry": "stub-global-registry",
        },
        key: [stub_extension],
    }
    result = helm.helm_template(chart_path, values)
    extensions = _get_extensions_of_job(helm, result)
    extension = extensions[0]
    assert extension["image"] == "stub-global-registry/stub-repository:stub-tag"


@pytest.mark.parametrize("key", ["extensions", "systemExtensions"])
def test_extension_image_with_global_registry_overwritten(helm, chart_path, key, stub_extension):
    values = {
        "global": {
            "imageRegistry": "stub-global-registry",
        },
        key: [stub_extension],
    }
    result = helm.helm_template(chart_path, values)
    extensions = _get_extensions_of_job(helm, result)
    extension = extensions[0]
    assert extension["image"] == "stub-registry/stub-repository:stub-tag"


def _get_extensions_of_job(helm, result):
    manifest = helm.get_resource(result, kind="Job")
    init_containers = findall(manifest, "spec.template.spec.initContainers")
    extensions = [c for c in init_containers if c["name"].endswith("-extension")]
    return extensions
