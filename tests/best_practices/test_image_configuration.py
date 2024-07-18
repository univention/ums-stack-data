# SPDX-FileCopyrightText: 2024 Univention GmbH
# SPDX-License-Identifier: AGPL-3.0-only

# Ruff has problems with multiline f-strings
# ruff: noqa: F541

import pytest
from yaml import safe_load

from utils import findall, findone


def test_global_registry_is_used_as_default(helm, chart_path):
    values = safe_load(
        """
        global:
          imageRegistry: "stub-global-registry"
    """,
    )
    result = helm.helm_template(chart_path, values)
    expected_registry = "stub-global-registry"
    containers = _get_containers_of_job(helm, result)
    _assert_all_images_use_registry(containers, expected_registry)


def test_image_registry_overrides_global_default_registry(helm, chart_path):
    values = safe_load(
        """
        global:
          imageRegistry: "stub-global-registry"

        image:
          registry: "stub-registry"
    """,
    )
    result = helm.helm_template(chart_path, values)
    expected_registry = "stub-registry"
    containers = _get_containers_of_job(helm, result)
    _assert_all_images_use_registry(containers, expected_registry)


def test_image_pull_secrets_can_be_provided(helm, chart_path):
    values = safe_load(
        """
        global:
          imagePullSecrets:
            - "stub-secret-a"
            - "stub-secret-b"
    """,
    )
    result = helm.helm_template(chart_path, values)
    manifest = helm.get_resource(result, kind="Job")

    expected_secrets = [
        {"name": "stub-secret-a"},
        {"name": "stub-secret-b"},
    ]
    image_pull_secrets = findone(manifest, "spec.template.spec.imagePullSecrets")
    assert image_pull_secrets == expected_secrets


def test_image_repository_can_be_configured(helm, chart_path):
    values = safe_load(
        """
        image:
          repository: "stub-fragment/stub-image"
    """,
    )
    result = helm.helm_template(chart_path, values)

    expected_repository = "stub-fragment/stub-image"
    containers = _get_containers_of_job(helm, result)
    _assert_all_images_contain(containers, expected_repository)


@pytest.mark.parametrize(
    "image_tag",
    [
        "stub_tag",
        "stub_tag@sha256:with-stub-digest-in-tag",
    ],
)
def test_image_tag_can_be_configured(image_tag, helm, chart_path):
    values = safe_load(
        f"""
        image:
          tag: "{image_tag}"
        """,
    )
    result = helm.helm_template(chart_path, values)

    expected_tag = image_tag
    containers = _get_containers_of_job(helm, result)
    _assert_all_images_contain(containers, expected_tag)


def test_all_image_values_are_configured(helm, chart_path):
    values = safe_load(
        f"""
        image:
          registry: "stub-registry.example"
          repository: "stub-fragment/stub-repository"
          tag: "stub-tag@sha256:stub-digest"
        """,
    )
    result = helm.helm_template(chart_path, values)

    expected_image = (
        "stub-registry.example/stub-fragment/"
        "stub-repository:stub-tag@sha256:stub-digest"
    )
    containers = _get_containers_of_job(helm, result)
    for container in containers:
        name = container["name"]
        image = container["image"]
        assert expected_image == image, f'Wrong image in container "{name}"'


def _assert_all_images_contain(containers, expected_value):
    for container in containers:
        name = container["name"]
        image = container["image"]
        assert expected_value in image, f'Wrong image value in container "{name}"'


def _assert_all_images_use_registry(containers, expected_registry):
    for container in containers:
        image = container["image"]
        name = container["name"]
        assert image.startswith(
            expected_registry + "/",
        ), f'Wrong registry in container "{name}"'


def _get_containers_of_job(helm, result):
    manifest = helm.get_resource(result, kind="Job")
    init_containers = findall(manifest, "spec.template.spec.initContainers")
    containers = findall(manifest, "spec.template.spec.containers")
    return init_containers + containers
