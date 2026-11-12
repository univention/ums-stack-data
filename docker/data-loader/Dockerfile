# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2024-2025 Univention GmbH

# Inspired by: https://hynek.me/articles/docker-uv/

ARG UCS_BASE_IMAGE_TAG=5.3.0-build.20261112@sha256:25e5e183b1b4f75c64e0c697d5795a8e9c15b935453c2a64406d7d1ab40b2214
ARG UCS_BASE_IMAGE=gitregistry.knut.univention.de/univention/dev/projects/ucs-base-image/ucs-base-python

###############################################
# Stage 1: build dependencies and software
FROM ${UCS_BASE_IMAGE}:${UCS_BASE_IMAGE_TAG} AS build
SHELL ["/bin/bash", "-uxo", "pipefail", "-c"]

COPY --from=ghcr.io/astral-sh/uv:0.13.7@sha256:96f40d3904aad8d0bd010539001d36c8e2188b981e1334471a90c4a1d93bb490 /uv /usr/local/bin/uv

ENV UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1 \
    UV_PYTHON_DOWNLOADS=never \
    UV_PYTHON=python3.13

COPY ./uv.lock \
     ./pyproject.toml \
     /app/

WORKDIR /app
RUN --mount=type=cache,target=/root/.cache \
  uv sync \
    --locked \
    --no-dev \
    --no-install-project && \
  uv export -o ./requirements.txt

# copy source code
COPY ./src /app/src

RUN uv sync --locked --no-dev --no-editable

###############################################
# Stage 2: final image
FROM ${UCS_BASE_IMAGE}:${UCS_BASE_IMAGE_TAG} AS final
SHELL ["/bin/bash", "-uxo", "pipefail", "-c"]

ENV PYTHONUNBUFFERED=1 \
    PATH=/app/.venv/bin:$PATH

ARG USER=data-loader
RUN rm -fr /var/lib/apt/lists/* /var/cache/apt/archives/* && \
    groupadd -r ${USER} -g 1000 && \
    useradd -r -d /app -g ${USER} -N ${USER} -u 1000 && \
    mkdir /join-data

COPY docker/data-loader/process-all.sh /usr/local/bin
COPY docker/data-loader/reload-udm-rest-api-cache.py /usr/local/bin
COPY docker/data-loader/wait-for-udm-rest-api.py /usr/local/bin
COPY docker/data-loader/set-data-loader-status-flag.yaml /

COPY --from=build --chown=${USER}:${USER} /app/requirements.txt /app/requirements.txt
COPY --from=build --chown=${USER}:${USER} /app/.venv /app/.venv

USER ${USER}

CMD ["process-all.sh"]

RUN \
  python3.13 -V && \
  python3.13 -m site && \
  python3.13 -c 'import univention.data_loader.cli'

###############################################
# Stage 3: testrunner image
FROM build AS test

ENV PYTHONUNBUFFERED=1 \
    PATH=/app/.venv/bin:$PATH

RUN --mount=type=cache,target=/root/.cache \
  uv sync --locked --dev

CMD ["pytest"]
