# Disclaimer - Work in progress

The repository you are looking into is work in progress.

It contains proof of concept and preview builds in development created in context of the [openDesk](https://gitlab.opencode.de/bmi/souveraener_arbeitsplatz/info) project.

The repository's content provides you with first insights into the containerized cloud IAM from Univention, derived from the UCS appliance.

# Stack Data Handling

The repository does contain tooling related to loading the initial data into the
container based stack.

## Status

Experimental

## Usage

The container `data-loader` provides the needed logic to load the initial data.
The container image itself does not bundle any data anymore.

The deployment has to ensure that the data is mounted into `/join-data`.

The Helm charts `stack-data-ums` and `stack-data-swp` are providing the data
through `ConfigMap` objects which are then mounted into the container.

The data import itself is triggered as `Job` objects in the Kubernetes cluster.

## Known limitations

- The password for `Administrator` has to be injected from the outside as a
  value to the Helm chart.
  - It would be preferable if a random password could be deployed and stored
    into a Secret object as an alternative option.
- `process-join-data.py` does not log the object name if the attribute is not
  called `name`, e.g. for users the attribute is called `username`.
- The configuration of the UMC Self-Service to find Memcached and PostgreSQL has
  to be provided via the values `stackDataContext.umcMemcachedHostname` and
  `stackDataContext.umcPostgresqlHostname` currently. These have to be kept in
  sync with the values used for the `umc-server` Helm chart.

## Development setup

Uses the Tilt based development environment at
<https://git.knut.univention.de/univention/customers/dataport/upx/dev-env>.
