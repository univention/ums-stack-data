# SPDX-FileCopyrightText: 2024-2025 Univention GmbH
# SPDX-License-Identifier: AGPL-3.0-only

from univention.testing.helm.best_practice.image_configuration import ImageConfiguration


class TestImageConfiguration(ImageConfiguration):
    def adjust_values(self, values: dict):
        image_configuration = values.get("image", {})

        # NOTE: Extensions are dynamic in nature, configure one stub extension
        # so that the generated init container will be checked as well.
        stub_extension = {
            "name": "stub-extension",
            "image": {
                "repository": "stub-path/stub-image",
                "tag": "stub-tag",
            }
            | image_configuration,
        }
        global_ = values.setdefault("global", {})
        global_["systemExtensions"] = [stub_extension]

        return values
