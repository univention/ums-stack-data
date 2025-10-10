# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2024-2025 Univention GmbH

# Inspired by: https://hynek.me/articles/docker-uv/

ARG UCS_BASE_IMAGE_TAG=5.2.3-build.20251009@sha256:8f67b1830e4f0c08843efec9309e0af97fe2f8e5ecb1d7c8959e9a18ab161852
ARG UCS_BASE_IMAGE=gitregistry.knut.univention.de/univention/dev/projects/ucs-base-image/ucs-base-python

###############################################
# Stage 1: build dependencies and software
FROM ${UCS_BASE_IMAGE}:${UCS_BASE_IMAGE_TAG} AS build
SHELL ["/bin/bash", "-uxo", "pipefail", "-c"]

COPY --from=ghcr.io/astral-sh/uv:0.6.3@sha256:8257f3d17fd04794feaf89d83b4ccca3b2eaa5501de9399fa53929843c0a5b55 /uv /usr/local/bin/uv

ENV UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1 \
    UV_PYTHON_DOWNLOADS=never \
    UV_PYTHON=python3.11

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
  python3.11 -V && \
  python3.11 -m site && \
  python3.11 -c 'import univention.data_loader.cli'

###############################################
# Stage 3: testrunner image
FROM build AS test

ENV PYTHONUNBUFFERED=1 \
    PATH=/app/.venv/bin:$PATH

RUN --mount=type=cache,target=/root/.cache \
  uv sync --locked --dev

CMD ["pytest"]
