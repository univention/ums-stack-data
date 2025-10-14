# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2025 Univention GmbH

from univention.testing.helm.auth_flavors.password_usage import AuthPasswordUsageViaVolume
from univention.testing.helm.auth_flavors.secret_generation import AuthSecretGenerationUser
from univention.testing.helm.auth_flavors.username import AuthUsernameViaConfigMap


class SettingsTestUdmSecret:
    secret_name = "release-name-stack-data-ums-udm"
    prefix_mapping = {
        "udm.auth": "auth",
    }

    # for AuthPasswordUsageViaVolume and AuthUsernameViaConfigMap
    workload_name = "release-name-stack-data-ums-1"
    workload_kind = "Job"


class TestChartCreatesUdmSecretAsUser(SettingsTestUdmSecret, AuthSecretGenerationUser):
    pass


class TestStackDataUsesUdmCredentialsByVolume(SettingsTestUdmSecret, AuthPasswordUsageViaVolume):
    volume_name = "secret-udm"


class TestStackDataUsesUdmUsernameByConfigMap(SettingsTestUdmSecret, AuthUsernameViaConfigMap):
    config_map_name = "release-name-stack-data-ums"
    path_username = "data.UDM_API_USER"
    default_username = "cn=admin"
