#!/bin/bash
# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2023 Univention GmbH


set -euo pipefail

echo "Load data scripts from /join-data:"
ls -l /join-data/

for data_file in $(find /join-data -type f | sort)
do
    echo
    process-join-data "$@" "${data_file}"
done

if [ ! -v UDM_API_USER ]; then
    echo "Not forcing cache reload for users/user module UDM REST API because UDM_API_USER is unset or empty"
else
    echo "Forcing cache reload for users/user module UDM REST API to reload extended_attributes"
    reload-udm-rest-api-cache.py
fi

if [[ "${SET_STATUS_FLAG:-false}" == true ]]; then
    echo "Set data loader status flag"
    process-join-data "$@" set-data-loader-status-flag.yaml
fi
