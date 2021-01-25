ARG BASE_IMAGE
FROM "${BASE_IMAGE}"

ARG DAGSTER_VERSION

# Checkout and install dagster libraries needed to run the gRPC server
# exposing your repository to dagit and dagster-daemon, and to load the DagsterInstance

# Use Virtual Environment
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"


# Install dependencies that are not in Pipfile
RUN pip install \
    dagster==${DAGSTER_VERSION} \
    dagster-postgres==${DAGSTER_VERSION} \
    dagster-docker==${DAGSTER_VERSION}

# Install dependencies that are in Pipfile
RUN pip install pipenv
COPY Pipfile* /tmp/
RUN cd /tmp && pipenv lock --keep-outdated --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt

# Set $DAGSTER_HOME and copy dagster instance there

ENV DAGSTER_HOME=/opt/dagster/dagster_home

RUN mkdir -p $DAGSTER_HOME

COPY docker/dagster.yaml $DAGSTER_HOME

# Add repository code

WORKDIR /opt/dagster/app

COPY definitions /opt/dagster/app/definitions

# Run dagster gRPC server on port 4000

EXPOSE 4000

# CMD allows this to be overridden from run launchers or executors that want
# to run other commands against your repository
CMD ["dagster", "api", "grpc", "-h", "0.0.0.0", "-p", "4000", "-f", "definitions/repositories.py"]
