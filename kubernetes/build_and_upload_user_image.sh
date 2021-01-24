cd ..
docker image build --build-arg DAGSTER_VERSION=0.10.1 --build-arg BASE_IMAGE=python:3.7.8-slim -f kubernetes/Dockerfile -t airblaster/dagster_exchangerates .
docker push airblaster/dagster_exchangerates