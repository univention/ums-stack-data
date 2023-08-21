---
date: 2023-08-21
deciders: jbornhold
status: accepted
---

# Use a custom script to wait for the UDM Rest API to be available


## Context

The jobs to load the data into the UMS stack require the UDM Rest API to be
available and ready to accept requests, otherwise we see errors being logged.

Simply waiting for the TCP port to be available and accepting connections was
not sufficient.


## Decision

For now a custom Python script is used to wait until it is possible to
successfully use `udm.get_ldap_base` from the UDM Rest API client object.


## Consequences

The main intended consequence is that operators will see a clear message about
waiting for the UDM Rest API instead of plenty of error messages.

The Job execution will only start after the UDM Rest API became available.

A slight drawback is that the configuration on the Kubernetes level is a little
bit more complex, since we are adding now an init container. The documentation
of Kubernetes states this to be a common pattern though.


## Pointers

- <https://kubernetes.io/docs/concepts/workloads/pods/init-containers/#init-containers-in-use>
