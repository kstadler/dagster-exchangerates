This project is an example for using https://dagster.io/.  
It retrieves exchange rates from the API at https://exchangeratesapi.io/ and stores them inside a sqlite database.

Current features:
- load exchange rates from exchangeratesapi.io
- default base currency is EUR but can be configured
- stores exchange rates in a sqlite database (please note that there are gaps for days without trade)
- year based partitions for use with CLI and dagit
- daily scheduler
- dagster type for the intermediate DataFrame with EventMetaData 
- run on console using preconfigured Python API example
- run using dagit
- planned: deploy using Docker Compose

This project uses pipenv for dependency management.

To run the project locally in the console using the Python API example use the follwoing commands:
```shell
pipenv install
pipenv run python example_run_without_docker.py
```
The parameters date_from and date_to are set statically in this example.

To run the dagit GUI for this project just run the following:

```shell
pipenv install
pipenv run dagit
```

This project is currently work in progress, support for Docker Compose is unfinished.