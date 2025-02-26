#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2023 Univention GmbH


import logging
from typing import Callable

from univention.admin.rest.client import UDM, NotFound, UnprocessableEntity

log = logging.getLogger(__name__)


ActionType = Callable[[UDM, str, str, dict, dict], None]


def ensure_udm_object(
    udm: UDM,
    module: str,
    position: str,
    properties: dict,
    policies: dict,
):
    log.info(f"Ensuring udm object {module}, {position}, {properties.get('name')}")
    module_obj = udm.get(module)
    obj = module_obj.new(position=position)
    obj.properties.update(properties)
    obj.policies.update(policies)
    try:
        obj.save()
    except UnprocessableEntity as exc:
        object_exists_message = '"dn" Object exists'
        # TODO: Find a more solid way to check if the object exists
        if object_exists_message in str(exc):
            log.info("Object does already exist, not updating anything.")
        else:
            raise


def upsert_udm_object(udm: UDM, module: str, position: str, properties, policies: dict):
    """
    Create a new UDM object or update it if it already exists.
    Handles both users/user and groups/group modules appropriately.
    """
    log.info(f"Ensuring udm object {module}, {position}")

    # Check for required identifier before proceeding
    try:
        dn_part = _get_dn_identifier_part(module, properties)
    except KeyError as e:
        # Re-raise the KeyError to maintain the expected error behavior
        raise KeyError(str(e))

    module_obj = udm.get(module)
    obj = module_obj.new(position=position)
    obj.properties.update(properties)
    obj.policies.update(policies)

    try:
        obj.save()
    except UnprocessableEntity as exc:
        object_exists_message = '"dn" Object exists'
        if object_exists_message not in str(exc):
            raise
        update_position = f"{dn_part},{position}"
        update_udm_object(udm, module, update_position, properties)


def update_udm_object(
    udm: UDM,
    module: str,
    position: str,
    properties: dict,
    policies: dict,
):
    log.info(f"Updating UDM object {module}, {position}")
    obj = udm.obj_by_dn(position)
    log.debug(f"Updating properties {list(properties.keys())}")
    obj.properties.update(properties)
    obj.policies.update(policies)
    obj.save()


def _get_dn_identifier_part(module, properties):
    """
    Get the DN identifier part based on the module type and properties.
    For users, it's uid=username, for groups it's cn=name
    """
    if module == "users/user":
        if "username" not in properties:
            raise KeyError("username")
        return f"uid={properties['username']}"
    elif module == "groups/group":
        if "name" not in properties:
            raise KeyError("name")
        return f"cn={properties['name']}"
    else:
        # For backward compatibility, default to using 'name' property with cn
        if "name" not in properties:
            raise KeyError("name")
        return f"cn={properties['name']}"


def modify_if_exists(
    udm: UDM,
    module: str,
    position: str,
    properties: dict,
    policies: dict,
):
    log.info(f"Modifying UDM object if exists: {module}, {position}")
    try:
        obj = udm.obj_by_dn(position)
        log.debug(f"Updating properties {list(properties.keys())}")
        obj.properties.update(properties)
        obj.policies.update(policies)
        obj.save()
    except NotFound:
        log.info(f"Object not found: {position}. No changes made.")


def delete_udm_object(
    udm: UDM,
    module: str,
    position,
    properties: dict,
    policies: dict,
):
    log.info(f"Deleting UDM object {module}, {position}")
    try:
        obj = udm.obj_by_dn(position)
        obj.delete()
    except NotFound:
        log.info("The object does not exist, not deleting anything.")


def ensure_list_contains(
    udm: UDM,
    module: str,
    position: str,
    properties: dict,
    policies,
):
    log.info(f"Ensuring attribute list contains value {module}, {position}")
    obj = udm.obj_by_dn(position)
    needs_save = False
    needs_save |= _ensure_values_in_dict(properties, obj.properties)
    needs_save |= _ensure_values_in_dict(policies, obj.policies)
    if needs_save:
        log.info(f'Saving object "{obj.dn}".')
        obj.save()
    else:
        log.info(f'No changes made to object "{obj.dn}".')


def _ensure_values_in_dict(values, obj_values):
    needs_save = False
    for name, value_list in values.items():
        log.info(
            f'Ensuring values "{value_list}" in "{name}".',
        )
        current_values = obj_values[name]
        for value in value_list:
            if value in current_values:
                log.debug(f'Value "{value}" already present in property "{name}".')
                continue
            log.debug(f'Adding value "{value}" into property "{name}".')
            current_values.append(value)
            needs_save = True
    return needs_save


def ensure_list_does_not_contain(
    udm: UDM,
    module: str,
    position: str,
    properties: dict,
    policies,
):
    log.info(f"Ensuring attribute list does not contain value {module}, {position}")
    obj = udm.obj_by_dn(position)
    needs_save = False
    needs_save |= _remove_values_from_dict(properties, obj.properties)
    needs_save |= _remove_values_from_dict(policies, obj.policies)
    if needs_save:
        log.info(f'Saving object "{obj.dn}".')
        obj.save()
    else:
        log.info(f'No changes made to object "{obj.dn}".')


def _remove_values_from_dict(values, obj_values):
    needs_save = False
    for name, values_list in values.items():
        log.info(f'Removing values "{values_list}" from "{name}" property.')
        current_values = obj_values[name]
        for value in values_list:
            if value not in current_values:
                log.debug(f'Value "{value}" not present in property "{name}".')
                continue
            log.debug(f'Removing value "{value}" from property "{name}".')
            current_values.remove(value)
            needs_save = True
    return needs_save


ACTIONS: dict[str, ActionType] = {
    "create": ensure_udm_object,
    "ensure_list_contains": ensure_list_contains,
    "ensure_list_does_not_contain": ensure_list_does_not_contain,
    "modify": update_udm_object,
    "modify_if_exists": modify_if_exists,
    "create_or_modify": upsert_udm_object,
    "delete_if_exists": delete_udm_object,
}


def get_action_runner(name: str) -> ActionType | None:
    return ACTIONS.get(name)
