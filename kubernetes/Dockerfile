ARG BASE_IMAGE
FROM "${BASE_IMAGE}"

ARG DAGSTER_VERSION

# ==> Add Dagster layer
RUN     apt-get update -yqq
# Cron
RUN     apt-get install -yqq cron

# Dagster
RUN     pip install \
        dagster==${DAGSTER_VERSION} \
        dagster-postgres==${DAGSTER_VERSION} \
        dagster-aws==${DAGSTER_VERSION} \
        dagster-k8s==${DAGSTER_VERSION} \
        dagster-pandas==${DAGSTER_VERSION} \
        requests \
        pandas

# Cleanup
RUN  rm -rf /var \
RUN  rm -rf /root/.cache  \
RUN  rm -rf /usr/lib/python2.7 \
RUN  rm -rf /usr/lib/x86_64-linux-gnu/guile

# ==> Add user code layer

WORKDIR /opt/dagster/app

COPY definitions /opt/dagster/app/definitions

