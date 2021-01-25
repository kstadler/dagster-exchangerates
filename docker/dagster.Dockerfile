# Dagster libraries to run both dagit and the dagster-daemon. Does not
# need to have access to any pipeline code.

ARG BASE_IMAGE
FROM "${BASE_IMAGE}"

ARG DAGSTER_VERSION

# Use Virtual Environment
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"


RUN pip install \
    dagster==${DAGSTER_VERSION} \
    dagster-graphql==${DAGSTER_VERSION} \
    dagster-postgres==${DAGSTER_VERSION} \
    dagster-docker==${DAGSTER_VERSION} \
    dagit==${DAGSTER_VERSION}

# Set $DAGSTER_HOME and copy dagster instance and workspace YAML there
ENV DAGSTER_HOME=/opt/dagster/dagster_home/

RUN mkdir -p $DAGSTER_HOME

COPY docker/dagster.yaml docker/workspace.yaml $DAGSTER_HOME

WORKDIR $DAGSTER_HOME
