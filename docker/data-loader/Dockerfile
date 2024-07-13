# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2023 Univention GmbH

ARG BASE_IMAGE_TAG=0.20.0-pre-jbornhold-refactor-udm-client
ARG BASE_IMAGE=gitregistry.knut.univention.de/univention/customers/dataport/upx/container-udm-rest/udm-rest-api-python-client:${BASE_IMAGE_TAG}


# hadolint ignore=DL3006
FROM ${BASE_IMAGE} as base

# hadolint ignore=DL3008
RUN apt-get --assume-yes --verbose-versions --no-install-recommends install \
      python3-pip \
      pipenv

WORKDIR /src

COPY Pipfile Pipfile.lock ./


FROM base as test

RUN pipenv sync --dev --system \
    && rm -r ~/.cache

WORKDIR /src/docker/data-loader

CMD ["pytest"]


# hadolint ignore=DL3006
FROM base as final

RUN pipenv sync --system \
    && rm -r ~/.cache

COPY bin/* /usr/local/bin/

WORKDIR /
RUN mkdir /join-data

COPY process-all.sh /
CMD ["/process-all.sh"]
