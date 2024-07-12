# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2024 Univention GmbH


def test_merges_simple_values(process_join_data):
    target = {"a": "stub_value"}
    source = {"b": "stub_value"}

    result = process_join_data.deep_merge(target, source)

    assert result == {"a": "stub_value", "b": "stub_value"}
