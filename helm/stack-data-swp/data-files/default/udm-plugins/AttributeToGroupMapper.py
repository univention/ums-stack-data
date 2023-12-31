"""
|UDM| hook definitions for modifying |LDAP| calls
when objects are created, modifier or deleted.
"""
# Copyright 2021-2022 Univention GmbH
#
# https://www.univention.de/
#
# All rights reserved.
#
# The source code of this program is made available
# under the terms of the GNU Affero General Public License version 3
# (GNU AGPL V3) as published by the Free Software Foundation.
#
# Binary versions of this program provided by Univention to you as
# well as other copyrighted, protected or trademarked materials like
# Logos, graphics, fonts, specific documentations and configurations,
# cryptographic keys etc. are subject to a license agreement between
# you and Univention and not subject to the GNU AGPL V3.
#
# In the case you use this program under the terms of the GNU AGPL V3,
# the program is provided in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License with the Debian GNU/Linux or Univention distribution in file
# /usr/share/common-licenses/AGPL-3; if not, see
# <https://www.gnu.org/licenses/>.

import json

import univention.debug as ud

from univention.admin.hook import simpleHook
from ldap.filter import filter_format

CONFIG_FILENAME = "/usr/share/attribute-to-group-mapper/flag_to_group_mapping.json"

DEBUG_PREFIX = "admin.hook.AttributeToGroupMapper"

try:
    flag_group_mapping = json.load(open(CONFIG_FILENAME))
except Exception as exc:
    flag_group_mapping = {}
    # debug is not yet initialized... thats bad...
    ud.debug(
        ud.ADMIN,
        ud.ERROR,
        f"{DEBUG_PREFIX}: could not open configuration file {CONFIG_FILENAME}: {exc}",
    )
if not all(
    isinstance(key, str) and isinstance(value, str)
    for key, value in flag_group_mapping.items()
):
    ud.debug(
        ud.ADMIN,
        ud.ERROR,
        f"{DEBUG_PREFIX}: invalid config file format {CONFIG_FILENAME}",
    )


class AttributeToGroupMapper(simpleHook):
    """
    Whenever a user is changed, get their app enabled flags.
    If the flags are set, we want to put them into a certain
    tenant specific group. That is important for portal tiles.
    """

    type = "AttributeToGroupMapper"

    def hook_ldap_pre_modify(self, obj):
        for attr, group in flag_group_mapping.items():
            groups = obj.lo.searchDn(
                filter_format("(&(cn=%s)(univentionObjectType=groups/group))", [group]),
            )
            if groups:
                group = groups[0]
            else:
                ud.debug(
                    ud.ADMIN,
                    ud.WARN,
                    f"{DEBUG_PREFIX}: There is no group {group}. Check your config",
                )
                continue
            value = obj[attr]
            add = value in ["OK", "TRUE", "1"]
            if add:
                if group not in obj["groups"]:
                    obj["groups"].append(group)
            else:
                if group in obj["groups"]:
                    obj["groups"].remove(group)

    hook_ldap_pre_create = hook_ldap_pre_modify
