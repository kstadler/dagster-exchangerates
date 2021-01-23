from dagster import repository

from .pipelines import exchangerates_pipline
from .partitions import year_partition_set


@repository
def exchangerates_repo():
    return [exchangerates_pipline, year_partition_set]
