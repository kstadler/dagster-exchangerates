This project is an example for using https://dagster.io/.  
It retrieves exchange rates from the API at https://exchangeratesapi.io/ and stores them inside a sqlite database.

Current features:
- load exchange rates from exchangeratesapi.io
- default base currency is EUR but can be configured
- stores exchange rates in a sqlite database (please note that there are gaps for days without trade)
- year based partitions for use with CLI and dagit
- daily scheduler
- Dagster type for the intermediate DataFrame with EventMetaData 
- run on console using preconfigured Python API example
- run using dagit
- deploy using Docker Compose
- deploy on Kubernetes using Helm
- Dagster version is pinned statically in various places (currently to v0.10.1)


This project uses pipenv for dependency management.

To run the project locally in the console using the Python API example use the follwoing commands:
```shell
pipenv install
cd local
pipenv run python local_example_run.py
```
The parameters date_from and date_to are set statically in this example.

To run the dagit GUI for this project just run the following:

```shell
pipenv install
cd local
pipenv run dagit
```

To deploy on Kubernetes using Helm do the following:
- setup your Kubernetes cluster and Helm 
  - this can be done on a local machine for testing purposes
  - on Windows you can setup Docker as a Kubernetes service and install Helm manually or using WSL
- deploy your usercode to docker using kubernetes/Dockerfile
  - adjust parameters in file kubernetes/versions 
  - run kubernetes/build_and_upload_user_image.py
- adjust parameters for Helm in kubernetes/values.yaml.
- install the Helm chart using the following commands:
  - `helm repo add dagster https://dagster-io.github.io/helm`
  - `helm upgrade --install --atomic dagster dagster/dagster -f ./values.yaml`
- forward the dagit port to http://localhost:8080 by running kubernetes/dagit.sh (Linux) or  kubernetes/dagit.bat (Windows)
