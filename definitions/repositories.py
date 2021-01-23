from dagster import repository

from definitions.exchangerates.pipelines import exchangerates_pipline
from definitions.exchangerates.partitions import year_partition_set


@repository
def exchangerates_repo():
    return [exchangerates_pipline, year_partition_set]
