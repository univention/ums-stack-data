# Stack Data Loader

This container is based on the `udm-rest-api-python-client` and bundles the
needed tooling to load initial data into one image. This way the data can be
initialized once the `udm-rest-api` is available.


## Status

This container requires that the data is provided by mounting it into the
directory `/join-data`.

This is an interim solution for the SouvAP project. On the short term we bundle
the fixed set of extensions and their related LDAP data into the images at build
time or provide them through the Helm charts. This allows us to move from the VM
into the fully containerized stack, even though the dynamic extension handling
is not yet solved for the container stack.


## Approach

The idea is, that every extension does provide its needs as a series of `YAML`
documents which describe which objects have to be present.

The utility script `project-join-data.py` is then used to apply those `YAML`
documents to the running `udm-rest-api`.

The `YAML` documents have to be mounted into `/join-data` and will be processed
from there.
