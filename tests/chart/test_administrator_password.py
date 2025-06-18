# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2025 Univention GmbH

import pytest

from univention.testing.helm.client.password import Password, PasswordOwner


class TestManagedPassoword(PasswordOwner, Password):
    secret_name = "release-name-stack-data-ums-administrator"

    derived_password = "00fc6a413808ae50b3026ee107d95367526a28fe"

    prefix_mapping = {
        "templateContext.initialPasswordAdministrator": "password",
    }

    @pytest.mark.skip(reason="TODO: Avoid that the password is templated")
    def test_password_is_not_templated():
        pass
