# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2024 Univention GmbH


def test_merges_simple_values(process_join_data):
    target = {"a": "stub_value"}
    source = {"b": "stub_value"}

    result = process_join_data.deep_merge(target, source)

    assert result == {"a": "stub_value", "b": "stub_value"}


def test_merges_nested_value(process_join_data):
    target = {"a": {"sub_a": "sub_a_value"}}
    source = {"a": {"merged_a": "merged_a_value"}}

    result = process_join_data.deep_merge(target, source)

    assert result == {"a": {"sub_a": "sub_a_value", "merged_a": "merged_a_value"}}


def test_replaces_lists(process_join_data):
    target = {"a_list": ["a"]}
    source = {"a_list": ["b"]}

    result = process_join_data.deep_merge(target, source)

    assert result == {"a_list": ["b"]}


def test_set_a_value_to_none(process_join_data):
    target = {"a": "stub_value"}
    source = {"a": None}

    result = process_join_data.deep_merge(target, source)

    assert result == {"a": None}
