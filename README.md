# Stack Data Handling

The repository does contain tooling related to loading the initial data into the
container based stack.

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
  - The Nubus umbrella helm charts by default generates a password
  from a common seed and injects it into this chart.
- `process-join-data.py` does not log the object name if the attribute is not
  called `name`, e.g. for users the attribute is called `username`.
- The configuration of the UMC Self-Service to find Memcached and PostgreSQL has
  to be provided via the values `stackDataContext.umcMemcachedHostname` and
  `stackDataContext.umcPostgresqlHostname` currently. These have to be kept in
  sync with the values used for the `umc-server` Helm chart.

## Development setup

Uses the Tilt based development environment at
<https://git.knut.univention.de/univention/customers/dataport/upx/dev-env>.

# Stack Data Loader

This container is based on the `udm-rest-api-python-client` and bundles the
needed tooling to load initial data into one image. This way the data can be
initialized once the `udm-rest-api` is available.

## Status

This container requires that the data is provided by mounting it into the
directory `/join-data`.

This container is a component of Nubus for initial bootstrapping of the
directory and for further updates from extensions and customization. It plugs
into the extension concept of Nubus.


## Approach

The idea is, that every extension does provide its needs as a series of `YAML`
documents which describe which operations have to be carried out.

The python executable `process-join-data` is then used to apply those `YAML`
documents to the running `udm-rest-api`. The utility script will perform the
following two steps:

- Load context and replace template variables in the files. Suggested is to
  mount the context files into `/template-context`.

- Process the result against the running `udm-rest-api`.

The `YAML` documents have to be mounted into `/join-data` and will be processed
from there.

The files are sorted based on the filename. A number based prefix shall be used
to avoid clashes due to implicit dependencies.


## Development

### Running the tests

```
docker compose run --build --rm -it data-loader-test
```


### Interacting with the script

```
docker compose run --build --rm -it data-loader-test bash

# inside of the container
bin/process-join-data.py --help
```

### Updating the Python dependencies

The dependencies are managed via `Pipenv` and can be updated as follows:

```
docker compose run -it --rm --build data-loader-test \
    pipenv update
```

Note that running the command inside of the container ensures that too recent
dependencies are excluded, those would require a more recent Python interpreter.

### Local development

Install `uv`: `pip install uv`
Create a virtualenv and install the project into it: `uv sync`
Activate the virtualenv `source .venv/bin/activate`

Run the tests: `pytest -v`

Run the data-loader: `data-loader`
