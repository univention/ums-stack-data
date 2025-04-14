# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2024-2025 Univention GmbH

import textwrap

import pytest


@pytest.fixture
def stub_data():
    """
    One item of data to process.
    """

    content = textwrap.dedent(
        """
        ---
        action: create
        module: portals/entry
        position: cn=entry,cn=portals,cn=univention,dc=univention-organization,dc=intranet
        properties:
          allowedGroups:
            - cn=Domain Users,cn=groups,dc=univention-organization,dc=intranet
          description:
            de_DE: Ihr Passwort ändern
            en_US: Change your password
          displayName:
            de_DE: Ihr Passwort ändern
            en_US: Change your password
          icon: ''
          link:
            - - en_US
              - '#/selfservice/passwordchange'
          linkTarget: samewindow
          name: self-service-password-change
    """,  # noqa: E501
    )
    return content
