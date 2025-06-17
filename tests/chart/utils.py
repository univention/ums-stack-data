# SPDX-FileCopyrightText: 2024-2025 Univention GmbH
# SPDX-License-Identifier: AGPL-3.0-only

import jsonpath


def findone(data, path):
    return jsonpath.match(path, data).obj


def findall(data, path):
    return jsonpath.match(path, data).obj


def get_containers_of_job(result):
    manifest = result.get_resource(kind="Job")
    init_containers = findall(manifest, "spec.template.spec.initContainers")
    containers = findall(manifest, "spec.template.spec.containers")
    return init_containers + containers
