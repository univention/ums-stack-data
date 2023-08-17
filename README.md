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

## Development setup

Uses the Tilt based development environment at
<https://git.knut.univention.de/univention/customers/dataport/upx/dev-env>.
