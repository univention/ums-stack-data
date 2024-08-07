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


## Details

- Many tests describe the relevant values fragment in YAML and parse it via
  `yaml.safe_load`. This shall help to make the example snippets comparable to
  an existing `values.yaml` for a Helm chart.
