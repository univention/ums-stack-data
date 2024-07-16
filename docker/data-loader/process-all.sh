#!/bin/bash
# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2023 Univention GmbH


set -euo pipefail

echo "Load data scripts from /join-data:"
ls -l /join-data/

for data_file in $(find /join-data -type f | sort)
do
    echo
    process-join-data.py "$@" "${data_file}"
done
