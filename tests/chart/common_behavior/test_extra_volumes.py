# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2025 Univention GmbH

from pytest_helm.utils import load_yaml

from univention.testing.helm.best_practice.extra_volumes import ExtraVolumes


class TestExtraVolumes(ExtraVolumes):
    # The plugin copying init containers only shuffle files, they get no extra mounts.
    containers_without_extra_volume_mounts = (
        "load-internal-plugins",
        "load-stub-extension-extension",
    )

    def adjust_values(self, values: dict):
        # Renders the plugin copying init containers, they are absent by default.
        values.update(
            load_yaml(
                """
                extensions:
                  - name: "stub-extension"
                    image:
                      registry: "stub-registry"
                      repository: "stub-repository"
                      tag: "stub-tag"
                """,
            ),
        )
        return values
