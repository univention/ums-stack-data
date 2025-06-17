# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2023-2025 Univention GmbH

from unittest import mock

import pytest
import yaml
from jinja2.exceptions import UndefinedError

from univention.admin.rest.client import NotFound, UnprocessableEntity
from univention.data_loader import actions, cli, process_template


@mock.patch("univention.data_loader.process_template.is_template")
@mock.patch("univention.data_loader.process_template.read_from_file")
def test_app_uses_template_extension(read_from_file_mock, is_template_mock, stub_data):
    read_from_file_mock.return_value = stub_data

    process_template.run(mock.Mock(), "stub-data.yaml", template_extension=".stub")

    is_template_mock.assert_called_once_with("stub-data.yaml", extension=".stub")


@mock.patch("univention.data_loader.process_template.render_template")
@mock.patch("univention.data_loader.process_template.read_from_file")
def test_app_renders_template_with_context(
    read_from_file_mock,
    render_template_mock,
    stub_data,
):
    read_from_file_mock.return_value = stub_data
    render_template_mock.return_value = stub_data

    context = {"stub_name": "stub_value"}
    process_template.run(mock.Mock(), "stub-data.yaml", template_context=context)

    render_template_mock.assert_called_once_with(stub_data, context)


def test_render_template_replaces_values():
    context = {"stub_name": "stub_value"}
    content = "{{ stub_name }}"

    result = process_template.render_template(content, context)

    assert result == "stub_value"


def test_render_template_fails_due_to_missing_variable():
    context = {}
    content = "{{ stub_name }}"

    with pytest.raises(UndefinedError):
        process_template.render_template(content, context)


@mock.patch("univention.data_loader.cli.deep_merge")
@mock.patch("univention.data_loader.cli.load_context")
def test_load_and_merge_contexts_uses_deep_merge(load_context_mock, deep_merge_mock):
    stub_context1 = {"stub_name1": "stub_value1"}
    stub_context2 = {"stub_name2": "stub_value2"}
    load_context_mock.side_effect = [stub_context1, stub_context2]

    cli.load_and_merge_contexts(["stub1.yaml", "stub2.yaml"])

    deep_merge_mock.assert_has_calls(
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
def test_load_context_reads_file(mocker, file_content):
    mock_open = mock.mock_open(read_data=file_content)
    mocker.patch.object(cli, "open", mock_open)

    result = cli.load_context("stub_context.yaml")

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
def test_is_template_is_by_default_always_true(filename, expected):
    result = process_template.is_template(filename)
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
):
    result = process_template.is_template(filename, extension="j2")
    assert result == expected


# @pytest.mark.skip()
# @mock.patch("univention.data_loader.actions.update_udm_object", autospec=True)
def test_process_action_handles_modify_action(mocker):
    update_udm_object_mock = mocker.Mock()
    mocker.patch.dict(actions.ACTIONS, {"modify": update_udm_object_mock})
    data = {
        "action": "modify",
        "module": "users/user",
        "position": "cn=admin,dc=base",
        "properties": {
            "firstname": "stub_firstname",
        },
    }
    process_template.process_action(mock.Mock(), data)
    update_udm_object_mock.assert_called_once()


def test_ensure_list_contains_adds_property():
    udm = mock.Mock()
    mock_obj = udm.obj_by_dn()
    mock_obj.properties = {
        "users": [],
    }

    properties = {
        "users": [
            "uid=Administrator,cn=users,dc=base",
        ],
    }
    policies = {}

    actions.ensure_list_contains(
        udm,
        "groups/group",
        "cn=Domain Users,dc=base",
        properties,
        policies,
    )
    assert "uid=Administrator,cn=users,dc=base" in mock_obj.properties["users"]
    mock_obj.save.assert_called()


def test_ensure_list_contains_skips_existing_property():
    udm = mock.Mock()
    mock_obj = udm.obj_by_dn()
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

    actions.ensure_list_contains(
        udm,
        "groups/group",
        "cn=Domain Users,dc=base",
        properties,
        policies,
    )
    assert len(mock_obj.properties["users"]) == 1
    mock_obj.save.assert_not_called()


def test_ensure_list_contains_adds_policy():
    udm = mock.Mock()
    mock_obj = udm.obj_by_dn()
    mock_obj.policies = {
        "policies/umc": [],
    }

    properties = {}
    policies = {
        "policies/umc": [
            "cn=default-umc-users,cn=UMC,cn=policies,dc=base",
        ],
    }

    actions.ensure_list_contains(
        udm,
        "groups/group",
        "cn=Domain Users,dc=base",
        properties,
        policies,
    )
    assert "cn=default-umc-users,cn=UMC,cn=policies,dc=base" in mock_obj.policies["policies/umc"]
    mock_obj.save.assert_called()


def test_ensure_list_contains_skips_existing_policy():
    udm = mock.Mock()
    mock_obj = udm.obj_by_dn()
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

    actions.ensure_list_contains(
        udm,
        "groups/group",
        "cn=Domain Users,dc=base",
        properties,
        policies,
    )
    assert len(mock_obj.policies["policies/umc"]) == 1
    mock_obj.save.assert_not_called()


def test_ensure_list_does_not_contain():
    udm = mock.Mock()
    mock_obj = udm.obj_by_dn()
    mock_obj.properties = {"users": ["user1", "user2", "user3"]}
    mock_obj.policies = {"policy": ["policy1", "policy2"]}

    properties = {"users": ["user2"]}
    policies = {"policy": ["policy1"]}

    actions.ensure_list_does_not_contain(
        udm,
        "groups/group",
        "cn=testgroup,dc=example,dc=com",
        properties,
        policies,
    )

    assert mock_obj.properties["users"] == ["user1", "user3"]
    assert mock_obj.policies["policy"] == ["policy2"]
    mock_obj.save.assert_called_once()


# def ensure_list_does_not_contain(self, module, position, properties, policies):
def test_ensure_list_does_not_contain_removes_property():
    udm = mock.Mock()
    mock_obj = udm.obj_by_dn()
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

    actions.ensure_list_does_not_contain(
        udm,
        "groups/group",
        "cn=Domain Users,dc=base",
        properties,
        policies,
    )
    assert "uid=stub_user,cn=users,dc=base" not in mock_obj.properties["users"]
    mock_obj.save.assert_called()


def test_ensure_list_does_not_contain_skips_missing_property():
    udm = mock.Mock()
    mock_obj = udm.obj_by_dn()
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

    actions.ensure_list_does_not_contain(
        udm,
        "groups/group",
        "cn=Domain Users,dc=base",
        properties,
        policies,
    )
    assert len(mock_obj.properties["users"]) == 1
    mock_obj.save.assert_not_called()


def test_ensure_list_does_not_contain_removes_policy():
    udm = mock.Mock()
    mock_obj = udm.obj_by_dn()
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

    actions.ensure_list_does_not_contain(
        udm,
        "groups/group",
        "cn=Domain Users,dc=base",
        properties,
        policies,
    )
    assert "cn=stub_policy,cn=UMC,cn=policies,dc=base" not in mock_obj.policies["policies/umc"]
    mock_obj.save.assert_called()


def test_ensure_list_does_not_contain_skips_missing_policy():
    udm = mock.Mock()
    mock_obj = udm.obj_by_dn()
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

    actions.ensure_list_does_not_contain(
        udm,
        "groups/group",
        "cn=Domain Users,dc=base",
        properties,
        policies,
    )
    assert len(mock_obj.policies["policies/umc"]) == 1
    mock_obj.save.assert_not_called()


def test_update_udm_object_sets_properties():
    udm = mock.Mock()
    mock_obj = udm.obj_by_dn()
    mock_obj.properties = {
        "firstname": "stub_firstname",
        "lastname": "stub_lastname",
    }

    properties = {
        "firstname": "new_firstname",
    }

    actions.update_udm_object(
        udm,
        "users/user",
        "cn=admin,dc=base",
        properties,
        {},
    )
    assert mock_obj.properties["firstname"] == "new_firstname"
    mock_obj.save.assert_called()


def test_delete_udm_object():
    udm = mock.Mock()
    mock_obj = udm.obj_by_dn()
    mock_obj.properties = {
        "firstname": "stub_firstname",
        "lastname": "stub_lastname",
    }
    actions.delete_udm_object(udm, "users/user", "cn=someuser,dc=base", {}, {})
    mock_obj.delete.assert_called()


def test_modify_if_exists_when_object_exists():
    udm = mock.Mock()
    mock_obj = udm.obj_by_dn()
    udm.obj_by_dn()

    properties = {"firstname": "John", "lastname": "Doe"}
    actions.modify_if_exists(
        udm,
        "users/user",
        "uid=johndoe,dc=example,dc=com",
        properties,
        {},
    )

    mock_obj.properties.update.assert_called_once_with(properties)
    mock_obj.save.assert_called_once()


def test_modify_if_exists_when_object_does_not_exist():
    # Create a proper NotFound exception with required arguments
    udm = mock.Mock()
    udm.obj_by_dn.side_effect = NotFound(
        code=404,
        message="Object not found",
        response=mock.Mock(),
    )

    properties = {"firstname": "John", "lastname": "Doe"}
    actions.modify_if_exists(
        udm,
        "users/user",
        "uid=johndoe,dc=example,dc=com",
        properties,
        {},
    )

    udm.obj_by_dn.assert_called_once()
    # Save should not be called since the object doesn't exist


@pytest.mark.parametrize(
    "module,properties,expected_dn_part",
    [
        (
            "users/user",
            {"username": "testuser", "firstname": "John", "lastname": "Doe"},
            "uid=testuser",
        ),
        (
            "groups/group",
            {"name": "testgroup", "description": "Test Group"},
            "cn=testgroup",
        ),
    ],
)
def test_create_or_modify_when_object_exists(module, properties, expected_dn_part):
    # Setup the mocks
    mock_module = mock.Mock()
    udm = mock.Mock()
    udm.get.return_value = mock_module
    mock_obj = mock.Mock()
    mock_module.new.return_value = mock_obj

    # Make save raise UnprocessableEntity to simulate existing object
    mock_obj.save.side_effect = UnprocessableEntity(
        code=422,
        message='"dn" Object exists',
        response=mock.Mock(),
    )

    position = "dc=example,dc=com"

    # Create a mock for update_udm_object
    with mock.patch.object(actions, "update_udm_object") as mock_update:
        actions.upsert_udm_object(udm, module, position, properties, {})

        # Verify the update_udm_object was called with correct parameters
        expected_position = f"{expected_dn_part},{position}"
        mock_update.assert_called_once_with(
            udm,
            module,
            expected_position,
            properties,
            {},
        )

    # Verify other expected calls
    mock_module.new.assert_called_once()
    mock_obj.save.assert_called_once()


@pytest.mark.parametrize(
    "module,properties",
    [
        (
            "users/user",
            {"username": "testuser", "firstname": "John", "lastname": "Doe"},
        ),
        (
            "groups/group",
            {"name": "testgroup", "description": "Test Group"},
        ),
    ],
)
def test_create_or_modify_when_object_does_not_exist(module, properties):
    # Setup mocks
    mock_module = mock.Mock()
    udm = mock.Mock()
    udm.get.return_value = mock_module
    mock_obj = mock.Mock()
    mock_module.new.return_value = mock_obj

    position = "dc=example,dc=com"

    # Call the function
    actions.upsert_udm_object(udm, module, position, properties, {})

    # Verify the expected calls
    mock_module.new.assert_called_once_with(position=position)
    mock_obj.properties.update.assert_called_once_with(properties)
    mock_obj.save.assert_called_once()


@pytest.mark.parametrize(
    "module,properties",
    [
        (
            "users/user",
            {"firstname": "John", "lastname": "Doe"},  # Missing username
        ),
        (
            "groups/group",
            {"description": "Test Group"},  # Missing name
        ),
    ],
)
def test_create_or_modify_fails_with_missing_identifier(module, properties):
    mock_module = mock.Mock()
    udm = mock.Mock()
    udm.get.return_value = mock_module

    with pytest.raises(KeyError) as exc_info:
        actions.upsert_udm_object(udm, module, "dc=example,dc=com", properties, {})

    expected_key = "username" if module == "users/user" else "name"
    assert str(exc_info.value) == f"\"'{expected_key}'\""
