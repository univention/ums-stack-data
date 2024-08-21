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

# FIXME: UDM REST API known issue
# https://git.knut.univention.de/univention/ucs/-/tree/5.2-0/management/univention-directory-manager-rest?ref_type=heads#known-issues
# The UDM REST API does not reload the extended_attributes cache after creating an extended_attribute.
# NOTE: This workaround forces the reload of the cache for the users/user module,
# and does 20 requests to ensure that we refresh all the round-robin replicas.
# It would be better to know the number of replicas and do that number of requests,
# or other approach.
if [ ! -v UDM_API_USER ]; then
    echo "Not forcing cache reload for users/user module UDM REST API because UDM_API_USER is unset or empty"
else
    echo "Forcing cache reload for users/user module UDM REST API to reload extended_attributes"
    for _ in seq 1 20;
    do
        curl \
            -X GET \
            -sS \
            -u "$UDM_API_USER:$(cat "$UDM_API_PASSWORD_FILE")" \
            -H "Accept: application/json" \
            "${UDM_API_URL}users/user/add";
    done
fi

if [[ "${SET_STATUS_FLAG:-false}" == true ]]; then
    echo "Set data loader status flag"
    process-join-data.py "$@" set-data-loader-status-flag.yaml
fi
