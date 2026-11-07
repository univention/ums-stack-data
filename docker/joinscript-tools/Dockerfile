# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2023-2025 Univention GmbH

ARG UCS_BASE_IMAGE=gitregistry.knut.univention.de/univention/dev/projects/ucs-base-image/ucs-base-python
ARG UCS_BASE_IMAGE_TAG=5.3.0-build.20261106@sha256:c59ae38f5a819046f9283904c4c64dbc9c77cf323173c44e4686db472334d184


FROM ${UCS_BASE_IMAGE}:${UCS_BASE_IMAGE_TAG}

RUN apt-get update \
    && apt-get --assume-yes --verbose-versions --no-install-recommends install \
      python3-univention-directory-manager-rest-client \
      python3-yaml \
      univention-config \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*

COPY bin/* /usr/local/bin/

COPY bin/fake.sh /usr/local/bin/die
COPY bin/fake.sh /usr/local/bin/joinscript_init
COPY bin/fake.sh /usr/local/bin/nc
COPY bin/fake.sh /usr/local/bin/systemctl
COPY bin/fake.sh /usr/local/bin/ucs_registerLDAPExtension
COPY bin/fake.sh /usr/local/bin/umc_init
COPY bin/fake.sh /usr/local/bin/umc_operation_create
COPY bin/fake.sh /usr/local/bin/univention-portal
