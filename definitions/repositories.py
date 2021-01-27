from dagster import repository

from definitions.exchangerates.pipelines import load_exchangerates_pipline
from definitions.exchangerates.partitions import load_exchangerates_year_partition_set
from definitions.exchangerates.schedules import load_exchangerates_schedule


@repository
def exchangerates_repo():
    return {
        "pipelines": {
            "exchangerates_pipline": load_exchangerates_pipline,
        },
        "partition_sets": {
            "exchangerates_year_partition_set": load_exchangerates_year_partition_set
        },
        "schedules": {"exchangerates_schedule": load_exchangerates_schedule},
    }
