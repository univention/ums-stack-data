ARG BASE_IMAGE_TAG=latest
ARG BASE_IMAGE=gitregistry.knut.univention.de/univention/customers/dataport/upx/container-udm-rest/udm-rest-api-python-client:${BASE_IMAGE_TAG}


# hadolint ignore=DL3006
FROM ${BASE_IMAGE} as test

RUN apt-get update \
    && apt-get --assume-yes --verbose-versions --no-install-recommends install \
      python3-pip=18.* \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/* \
    && pip3 install --no-cache-dir pipenv==2023.6.18

WORKDIR /src

COPY Pipfile Pipfile.lock ./

RUN pipenv sync --dev --system \
    && rm -r ~/.cache

WORKDIR /src/docker/data-loader

CMD ["pytest"]


# hadolint ignore=DL3006
FROM ${BASE_IMAGE} as final

COPY bin/* /usr/local/bin

WORKDIR /
RUN mkdir /join-data

COPY process-all.sh /
CMD ["/process-all.sh"]
