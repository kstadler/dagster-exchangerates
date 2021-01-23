from datetime import datetime, date

from dagster import PartitionSetDefinition


def get_year_partitions():
    current_year = datetime.now().year

    partitions = []
    for year in range(current_year, 1999, -1):
        partitions.append(str(year))
    return partitions


def run_config_for_year_partition(partition):
    year = int(partition.value)
    date_from = date(year=year, month=1, day=1).isoformat()
    date_to = date(year=year, month=12, day=31).isoformat()
    return {"solids": {"extract": {"config": {"date_from": date_from, "date_to": date_to}}}}


year_partition_set = PartitionSetDefinition(
    name="year_partition_set",
    pipeline_name="exchangerates_pipline",
    partition_fn=get_year_partitions,
    run_config_fn_for_partition=run_config_for_year_partition,
)
