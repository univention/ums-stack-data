# SPDX-FileCopyrightText: 2024-2025 Univention GmbH
# SPDX-License-Identifier: AGPL-3.0-only

def get_containers_of_job(result):
    manifest = result.get_resource(kind="Job")
    init_containers = manifest.findone("spec.template.spec.initContainers")
    containers = manifest.findone("spec.template.spec.containers")
    return init_containers + containers
