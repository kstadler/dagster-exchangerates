from datetime import date

from dagster import PartitionSetDefinition

from definitions.common.partitions import get_year_partitions


def run_config_for_year_partition(partition):
    year = int(partition.value)
    date_from = date(year=year, month=1, day=1).isoformat()
    date_to = date(year=year, month=12, day=31).isoformat()
    return {
        "solids": {"extract": {"config": {"date_from": date_from, "date_to": date_to}}}
    }


def load_exchangerates_year_partition_set():
    return PartitionSetDefinition(
        name="exchangerates_year_partition_set",
        pipeline_name="exchangerates_pipline",
        partition_fn=get_year_partitions,
        run_config_fn_for_partition=run_config_for_year_partition,
    )
