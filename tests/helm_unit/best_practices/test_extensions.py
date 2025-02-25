# SPDX-FileCopyrightText: 2024 Univention GmbH
# SPDX-License-Identifier: AGPL-3.0-only

# Ruff has problems with multiline f-strings
# ruff: noqa: F541

import copy

import pytest
from yaml import safe_load

from ..utils import findall

ALL_EXTENSION_KEYS = (
    "extensions",
    "systemExtensions",
    "global.extensions",
    "global.systemExtensions",
)


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


@pytest.mark.parametrize("key", ALL_EXTENSION_KEYS)
def test_extension_configured(helm, chart_path, key, stub_extension):
    values = {}
    _set_dot_path_value(values, key, [stub_extension])

    result = helm.helm_template(chart_path, values)
    extensions = _get_extensions_of_job(helm, result)
    assert len(extensions) == 1

    extension = extensions[0]
    assert extension["name"] == "load-stub-test-extension"


def test_custom_and_system_extensions_are_joined(helm, chart_path, stub_extension):
    stub_system_extension = copy.deepcopy(stub_extension)
    stub_system_extension["name"] = "stub-system"
    values = {
        "extensions": [stub_extension],
        "systemExtensions": [stub_system_extension],
    }

    result = helm.helm_template(chart_path, values)
    extensions = _get_extensions_of_job(helm, result)
    extension_names = [e["name"] for e in extensions]
    assert extension_names == ["load-stub-system-extension", "load-stub-test-extension"]


@pytest.mark.parametrize("key", ALL_EXTENSION_KEYS)
def test_extension_image(helm, chart_path, key, stub_extension):
    values = {}
    _set_dot_path_value(values, key, [stub_extension])
    result = helm.helm_template(chart_path, values)
    extensions = _get_extensions_of_job(helm, result)
    extension = extensions[0]
    assert extension["image"] == "stub-registry/stub-repository:stub-tag"


@pytest.mark.parametrize("key", ALL_EXTENSION_KEYS)
def test_extension_image_with_global_registry(helm, chart_path, key, stub_extension):
    del stub_extension["image"]["registry"]
    values = {
        "global": {
            "imageRegistry": "stub-global-registry",
        },
    }
    _set_dot_path_value(values, key, [stub_extension])
    result = helm.helm_template(chart_path, values)
    extensions = _get_extensions_of_job(helm, result)
    extension = extensions[0]
    assert extension["image"] == "stub-global-registry/stub-repository:stub-tag"


@pytest.mark.parametrize("key", ALL_EXTENSION_KEYS)
def test_extension_image_with_global_registry_overwritten(
    helm,
    chart_path,
    key,
    stub_extension,
):
    values = {
        "global": {
            "imageRegistry": "stub-global-registry",
        },
    }
    _set_dot_path_value(values, key, [stub_extension])
    result = helm.helm_template(chart_path, values)
    extensions = _get_extensions_of_job(helm, result)
    extension = extensions[0]
    assert extension["image"] == "stub-registry/stub-repository:stub-tag"


@pytest.mark.parametrize("key", ["extensions", "systemExtensions"])
def test_local_configuration_overrides_global_configuration(
    helm,
    chart_path,
    key,
    stub_extension,
):
    stub_global_extension = {
        **stub_extension,
        "name": "stub-global",
    }
    values = {
        "global": {
            key: [stub_global_extension],
        },
        key: [stub_extension],
    }
    result = helm.helm_template(chart_path, values)
    extensions = _get_extensions_of_job(helm, result)
    assert len(extensions) == 1
    assert extensions[0]["name"] == "load-stub-test-extension"


def _get_extensions_of_job(helm, result):
    manifest = helm.get_resource(result, kind="Job")
    init_containers = findall(manifest, "spec.template.spec.initContainers")
    extensions = [c for c in init_containers if c["name"].endswith("-extension")]
    return extensions


def _set_dot_path_value(target, key, value):
    scope = target
    key_path = key.split(".")
    for fragment in key_path[:-1]:
        scope = scope.setdefault(fragment, {})
    scope[key_path[-1]] = value
