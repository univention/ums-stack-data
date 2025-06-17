# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2025 Univention GmbH

from univention.testing.helm.client.udm import UdmClient


class TestAuth(UdmClient):
    config_map_name = "release-name-stack-data-ums"
    secret_name = "release-name-stack-data-ums-udm"
    workload_kind = "Job"

    default_username = "cn=admin"

    path_udm_api_username = "data.UDM_API_USER"
