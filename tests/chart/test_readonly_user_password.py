# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2025 Univention GmbH

import pytest
from univention.testing.helm.client.password import Password, PasswordOwner


class TestManagedPassoword(PasswordOwner, Password):
    secret_name = "release-name-stack-data-ums-readonly-user"

    derived_password = "c5fbd455a487b4a5d21d90374fb994551dd6c5d2"

    prefix_mapping = {
        "templateContext.readonlyUserPassword": "password",
    }

    @pytest.mark.skip(reason="TODO: Avoid that the password is templated")
    def test_password_is_not_templated():
        pass
