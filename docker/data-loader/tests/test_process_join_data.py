# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2023 Univention GmbH

from unittest import mock

import pytest
import yaml
from jinja2.exceptions import UndefinedError


@pytest.fixture
def app(process_join_data):
    mock_udm = mock.Mock()
    return process_join_data.App(mock_udm)


def test_app_uses_template_extension(process_join_data, mocker, stub_data):
    mocker.patch.object(process_join_data, "read_from_file", return_value=stub_data)
    is_template_mock = mocker.patch.object(process_join_data, "is_template")
    app = process_join_data.App(mock.Mock(), template_extension=".stub")

    app.run("stub-data.yaml")

    is_template_mock.assert_called_once_with("stub-data.yaml", extension=".stub")


def test_app_renders_template_with_context(process_join_data, mocker, stub_data):
    mocker.patch.object(process_join_data, "read_from_file", return_value=stub_data)
    render_template_mock = mocker.patch.object(
        process_join_data,
        "render_template",
        return_value=stub_data,
    )
    context = {"stub_name": "stub_value"}
    app = process_join_data.App(mock.Mock(), template_context=context)

    app.run("stub-data.yaml")

    render_template_mock.assert_called_once_with(stub_data, context)


def test_render_template_replaces_values(process_join_data):
    context = {"stub_name": "stub_value"}
    content = "{{ stub_name }}"

    result = process_join_data.render_template(content, context)

    assert result == "stub_value"


def test_render_template_fails_due_to_missing_variable(process_join_data):
    context = {}
    content = "{{ stub_name }}"

    with pytest.raises(UndefinedError):
        process_join_data.render_template(content, context)


def test_load_and_merge_contexts_uses_deep_merge(process_join_data, mocker):
    stub_context1 = {"stub_name1": "stub_value1"}
    stub_context2 = {"stub_name2": "stub_value2"}
    mocker.patch.object(
        process_join_data,
        "load_context",
        side_effect=[stub_context1, stub_context2],
    )
    merge_context_mock = mocker.patch.object(process_join_data, "deep_merge")

    process_join_data.load_and_merge_contexts(["stub1.yaml", "stub2.yaml"])

    merge_context_mock.assert_has_calls(
        [
            mock.call(mock.ANY, stub_context1),
            mock.call(mock.ANY, stub_context2),
        ],
    )


@pytest.mark.parametrize(
    "file_content",
    [
        "stub_name: stub_value",
        "stub_name2: stub_value2",
    ],
)
def test_load_context_reads_file(process_join_data, mocker, file_content):
    mock_open = mock.mock_open(read_data=file_content)
    mocker.patch.object(process_join_data, "open", mock_open)

    result = process_join_data.load_context("stub_context.yaml")

    mock_open.assert_called_once_with("stub_context.yaml", "r")
    expected_context = yaml.safe_load(file_content)
    assert result == expected_context


@pytest.mark.parametrize(
    "filename,expected",
    [
        ("my-join-data.yaml", True),
        ("my-join-data.yaml.j2", True),
    ],
)
def test_is_template_is_by_default_always_true(filename, expected, process_join_data):
    result = process_join_data.is_template(filename)
    assert result == expected


@pytest.mark.parametrize(
    "filename,expected",
    [
        ("my-join-data.yaml", False),
        ("my-join-data.yaml.j2", True),
    ],
)
def test_is_template_can_be_limited_to_filename_extension(
    filename,
    expected,
    process_join_data,
):
    result = process_join_data.is_template(filename, extension="j2")
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


def test_remove_from_list_removes_property(app):
    mock_obj = app.udm.obj_by_dn()
    mock_obj.properties = {
        "users": [
            "uid=Administrator,cn=users,dc=base",
            "uid=stub_user,cn=users,dc=base",
        ],
    }
    properties = {
        "users": [
            "uid=stub_user,cn=users,dc=base",
        ],
    }
    policies = {}

    app.remove_from_list(
        "groups/group",
        "cn=Domain Users,dc=base",
        properties,
        policies,
    )
    assert "uid=stub_user,cn=users,dc=base" not in mock_obj.properties["users"]
    mock_obj.save.assert_called()


def test_remove_from_list_skips_missing_property(app):
    mock_obj = app.udm.obj_by_dn()
    mock_obj.properties = {
        "users": [
            "uid=Administrator,cn=users,dc=base",
        ],
    }
    properties = {
        "users": [
            "uid=stub_user,cn=users,dc=base",
        ],
    }
    policies = {}

    app.remove_from_list(
        "groups/group",
        "cn=Domain Users,dc=base",
        properties,
        policies,
    )
    assert len(mock_obj.properties["users"]) == 1
    mock_obj.save.assert_not_called()


def test_remove_from_list_removes_policy(app):
    mock_obj = app.udm.obj_by_dn()
    mock_obj.policies = {
        "policies/umc": [
            "cn=default-umc-users,cn=UMC,cn=policies,dc=base",
            "cn=stub_policy,cn=UMC,cn=policies,dc=base",
        ],
    }
    properties = {}
    policies = {
        "policies/umc": [
            "cn=stub_policy,cn=UMC,cn=policies,dc=base",
        ],
    }

    app.remove_from_list(
        "groups/group",
        "cn=Domain Users,dc=base",
        properties,
        policies,
    )
    assert (
        "cn=stub_policy,cn=UMC,cn=policies,dc=base"
        not in mock_obj.policies["policies/umc"]
    )
    mock_obj.save.assert_called()


def test_remove_from_list_skips_missing_policy(app):
    mock_obj = app.udm.obj_by_dn()
    mock_obj.policies = {
        "policies/umc": [
            "cn=default-umc-users,cn=UMC,cn=policies,dc=base",
        ],
    }
    properties = {}
    policies = {
        "policies/umc": [
            "cn=stub_policy,cn=UMC,cn=policies,dc=base",
        ],
    }

    app.remove_from_list(
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
