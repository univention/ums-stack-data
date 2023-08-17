#!/bin/bash

set -euo pipefail

echo "Load data scripts from /join-data:"
ls -l /join-data/

for data_file in $(find /join-data -type f | sort)
do
    echo "Processing ${data_file}"
    process-join-data.py "${data_file}"
done
