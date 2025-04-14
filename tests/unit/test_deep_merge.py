# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2024-2025 Univention GmbH

from univention.data_loader.cli import deep_merge


def test_merges_simple_values():
    target = {"a": "stub_value"}
    source = {"b": "stub_value"}

    deep_merge(target, source)

    assert target == {"a": "stub_value", "b": "stub_value"}


def test_merges_nested_value():
    target = {"a": {"sub_a": "sub_a_value"}}
    source = {"a": {"merged_a": "merged_a_value"}}

    deep_merge(target, source)

    assert target == {"a": {"sub_a": "sub_a_value", "merged_a": "merged_a_value"}}


def test_replaces_lists():
    target = {"a_list": ["a"]}
    source = {"a_list": ["b"]}

    deep_merge(target, source)

    assert target == {"a_list": ["b"]}


def test_set_a_value_to_none():
    target = {"a": "stub_value"}
    source = {"a": None}

    deep_merge(target, source)

    assert target == {"a": None}
