ARG BASE_IMAGE
FROM "${BASE_IMAGE}"

ARG DAGSTER_VERSION

# ==> Add Dagster layer
RUN     apt-get update -yqq
# Cron
RUN     apt-get install -yqq cron

# Use Virtual Environment
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies that are not in Pipfile
RUN     pip install \
        dagster==${DAGSTER_VERSION} \
        dagster-postgres==${DAGSTER_VERSION} \
        dagster-k8s==${DAGSTER_VERSION}

# Install dependencies that are in Pipfile
RUN pip install pipenv
COPY Pipfile* /tmp/
RUN cd /tmp && pipenv lock --keep-outdated --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt

# Cleanup
RUN  rm -rf /var \
RUN  rm -rf /root/.cache  \
RUN  rm -rf /usr/lib/python2.7 \
RUN  rm -rf /usr/lib/x86_64-linux-gnu/guile

# ==> Add user code layer

WORKDIR /opt/dagster/app

COPY definitions /opt/dagster/app/definitions

