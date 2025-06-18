# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2025 Univention GmbH

import pytest

from univention.testing.helm.client.password import Password, PasswordOwner


class TestManagedPassoword(PasswordOwner, Password):
    secret_name = "release-name-stack-data-ums-svc-portal-server"

    derived_password = "df0b6e0881dfea413816f89b7fb793b13ad60c32"

    prefix_mapping = {
        "templateContext.svcPortalServerUserPassword": "password",
    }

    @pytest.mark.skip(reason="TODO: Avoid that the password is templated")
    def test_password_is_not_templated():
        pass
