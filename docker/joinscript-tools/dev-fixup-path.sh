# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2023-2025 Univention GmbH

# shellcheck shell=bash

# This file has to be sourced to update the path
#
# Indented usage is for testing out the tooling locally. With the adjusted PATH
# the scripts will run directly out of the sources if mounted correctly into the
# container.
export PATH=/src/docker/udm-rest-api-joinscript-tools/bin:$PATH
