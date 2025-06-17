# SPDX-FileCopyrightText: 2024-2025 Univention GmbH
# SPDX-License-Identifier: AGPL-3.0-only

# Ruff has problems with multiline f-strings
# ruff: noqa: F541

import pytest
from pytest_helm.utils import get_containers, load_yaml


def test_global_registry_is_used_as_default(chart):
    values = load_yaml(
        """
        global:
          imageRegistry: "stub-global-registry"
    """,
    )
    result = chart.helm_template(values)
    expected_registry = "stub-global-registry"
    _assert_all_images_use_registry(result, expected_registry)


def test_image_registry_overrides_global_default_registry(chart):
    values = load_yaml(
        """
        global:
          imageRegistry: "stub-global-registry"

        image:
          registry: "stub-registry"
    """,
    )
    result = chart.helm_template(values)
    expected_registry = "stub-registry"
    _assert_all_images_use_registry(result, expected_registry)


def test_global_pull_policy_is_used(chart):
    values = load_yaml(
        """
        global:
          imagePullPolicy: "stub-global-pull-policy"
    """,
    )
    result = chart.helm_template(values)
    expected_pull_policy = "stub-global-pull-policy"
    _assert_all_images_use_pull_policy(result, expected_pull_policy)


def test_image_pull_policy_overrides_global_value(chart):
    values = load_yaml(
        """
        global:
          imagePullPolicy: "stub-global-pull-policy"

        image:
          imagePullPolicy: "stub-pull-policy"
    """,
    )
    result = chart.helm_template(values)
    expected_pull_policy = "stub-pull-policy"
    _assert_all_images_use_pull_policy(result, expected_pull_policy)


def test_image_pull_secrets_can_be_provided(chart):
    values = load_yaml(
        """
        global:
          imagePullSecrets:
            - "stub-secret-a"
            - "stub-secret-b"
    """,
    )
    result = chart.helm_template(values)
    manifest = result.get_resource(kind="Job")

    expected_secrets = [
        {"name": "stub-secret-a"},
        {"name": "stub-secret-b"},
    ]
    image_pull_secrets = manifest.findone("spec.template.spec.imagePullSecrets")
    assert image_pull_secrets == expected_secrets


def test_image_repository_can_be_configured(chart):
    values = load_yaml(
        """
        image:
          repository: "stub-fragment/stub-image"
    """,
    )
    result = chart.helm_template(values)

    expected_repository = "stub-fragment/stub-image"
    _assert_all_images_contain(result, expected_repository)


@pytest.mark.parametrize(
    "image_tag",
    [
        "stub_tag",
        "stub_tag@sha256:with-stub-digest-in-tag",
    ],
)
def test_image_tag_can_be_configured(image_tag, chart):
    values = load_yaml(
        f"""
        image:
          tag: "{image_tag}"
        """,
    )
    result = chart.helm_template(values)

    expected_tag = image_tag
    _assert_all_images_contain(result, expected_tag)


def test_all_image_values_are_configured(chart):
    values = load_yaml(
        f"""
        image:
          registry: "stub-registry.example"
          repository: "stub-fragment/stub-repository"
          tag: "stub-tag@sha256:stub-digest"
        """,
    )
    result = chart.helm_template(values)

    expected_image = "stub-registry.example/stub-fragment/" "stub-repository:stub-tag@sha256:stub-digest"
    job = result.get_resource(kind="Job")
    containers = get_containers(job)
    for container in containers:
        name = container["name"]
        image = container["image"]
        assert expected_image == image, f'Wrong image in container "{name}"'


def _assert_all_images_contain(result, expected_value):
    job = result.get_resource(kind="Job")
    containers = get_containers(job)
    for container in containers:
        name = container["name"]
        image = container["image"]
        assert expected_value in image, f'Wrong image value in container "{name}"'


def _assert_all_images_use_registry(result, expected_registry):
    job = result.get_resource(kind="Job")
    containers = get_containers(job)
    for container in containers:
        image = container["image"]
        name = container["name"]
        assert image.startswith(
            expected_registry + "/",
        ), f'Wrong registry in container "{name}"'


def _assert_all_images_use_pull_policy(result, expected_pull_policy):
    job = result.get_resource(kind="Job")
    containers = get_containers(job)
    for container in containers:
        pull_policy = container["imagePullPolicy"]
        name = container["name"]
        assert pull_policy == expected_pull_policy, f'Wrong imagePullPolicy in container "{name}"'
