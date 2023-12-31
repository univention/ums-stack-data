# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2023 Univention GmbH

import importlib.util
import os
import os.path
from unittest import mock

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
def app(process_join_data):
    mock_udm = mock.Mock()
    return process_join_data.App(mock_udm)


@pytest.mark.parametrize(
    "filename,expected",
    [
        ("my-join-data.yaml", False),
        ("my-join-data.yaml.j2", True),
    ],
)
def test_is_template(filename, expected, process_join_data):
    result = process_join_data.is_template(filename)
    assert result == expected


def test_process_action_handles_modify_action(mocker, app):
    update_udm_object = mocker.patch.object(app, "update_udm_object", autospec=True)
    data = {
        "action": "modify",
        "module": "users/user",
        "position": "cn=admin,dc=base",
        "properties": {
            "firstname": "stub_firstname",
        },
    }
    app.process_action(data)
    update_udm_object.assert_called_once()


def test_ensure_list_contains_adds_property(app):
    mock_obj = app.udm.obj_by_dn()
    mock_obj.properties = {
        "users": [],
    }

    properties = {
        "users": [
            "uid=Administrator,cn=users,dc=base",
        ],
    }
    policies = {}

    app.ensure_list_contains(
        "groups/group",
        "cn=Domain Users,dc=base",
        properties,
        policies,
    )
    assert "uid=Administrator,cn=users,dc=base" in mock_obj.properties["users"]
    mock_obj.save.assert_called()


def test_ensure_list_contains_skips_existing_property(app):
    mock_obj = app.udm.obj_by_dn()
    mock_obj.properties = {
        "users": [
            "uid=Administrator,cn=users,dc=base",
        ],
    }

    properties = {
        "users": [
            "uid=Administrator,cn=users,dc=base",
        ],
    }
    policies = {}

    app.ensure_list_contains(
        "groups/group",
        "cn=Domain Users,dc=base",
        properties,
        policies,
    )
    assert len(mock_obj.properties["users"]) == 1
    mock_obj.save.assert_not_called()


def test_ensure_list_contains_adds_policy(app):
    mock_obj = app.udm.obj_by_dn()
    mock_obj.policies = {
        "policies/umc": [],
    }

    properties = {}
    policies = {
        "policies/umc": [
            "cn=default-umc-users,cn=UMC,cn=policies,dc=base",
        ],
    }

    app.ensure_list_contains(
        "groups/group",
        "cn=Domain Users,dc=base",
        properties,
        policies,
    )
    assert (
        "cn=default-umc-users,cn=UMC,cn=policies,dc=base"
        in mock_obj.policies["policies/umc"]
    )
    mock_obj.save.assert_called()


def test_ensure_list_contains_skips_existing_policy(app):
    mock_obj = app.udm.obj_by_dn()
    mock_obj.policies = {
        "policies/umc": [
            "cn=default-umc-users,cn=UMC,cn=policies,dc=base",
        ],
    }

    properties = {}
    policies = {
        "policies/umc": [
            "cn=default-umc-users,cn=UMC,cn=policies,dc=base",
        ],
    }

    app.ensure_list_contains(
        "groups/group",
        "cn=Domain Users,dc=base",
        properties,
        policies,
    )
    assert len(mock_obj.policies["policies/umc"]) == 1
    mock_obj.save.assert_not_called()


def test_update_udm_object_sets_properties(app):
    mock_obj = app.udm.obj_by_dn()
    mock_obj.properties = {
        "firstname": "stub_firstname",
        "lastname": "stub_lastname",
    }

    properties = {
        "firstname": "new_firstname",
    }

    app.update_udm_object(
        "users/user",
        "cn=admin,dc=base",
        properties,
    )
    assert mock_obj.properties["firstname"] == "new_firstname"
    mock_obj.save.assert_called()


def test_delete_udm_object(app):
    mock_obj = app.udm.obj_by_dn()
    mock_obj.properties = {
        "firstname": "stub_firstname",
        "lastname": "stub_lastname",
    }
    app.delete_udm_object("users/user", "cn=someuser,dc=base")
    mock_obj.delete.assert_called()
