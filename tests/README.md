# Unittests

This folder contains a set of unit tests which cover the behavior of the charts.


## Requirements

- `docker compose` has to be set up and working


## How to run this manually

```
# Run the test suite
docker compose run -it --rm test

# Deal with trouble via pdb
docker compose run -it --rm test pytest tests --pdb

# Have a shell
docker compose run -it --rm test bash
```
