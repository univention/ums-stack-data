# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2024 Univention GmbH

import importlib.util
import os
import os.path
import textwrap

import pytest


@pytest.fixture
def process_join_data():
    """Provide "process-join-data.py" as a module."""
    module_name = "process_join_data"
    module_path = "./bin/process-join-data.py"
    spec = importlib.util.spec_from_file_location(
        module_name,
        os.path.join(module_path),
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


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
