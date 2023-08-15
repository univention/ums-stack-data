#!/bin/bash

echo "Load data scripts from /join-data:"
ls -l /join-data/

find /join-data -type f | sort | xargs --no-run-if-empty --max-args=1 --verbose process-join-data.py
