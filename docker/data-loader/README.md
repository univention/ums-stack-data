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

The utility script `process-join-data.py` is then used to apply those `YAML`
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
