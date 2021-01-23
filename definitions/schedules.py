from datetime import datetime, date

from dagster import daily_schedule


@daily_schedule(
    pipeline_name="exchangerates_pipline",
    start_date=datetime(2020, 1, 1),
    execution_timezone="CET",
)
def my_daily_schedule(day: datetime):
    year = day.year
    date_from = date(year=year, month=1, day=1).isoformat()
    date_to = date(year=year, month=12, day=31).isoformat()
    return {"solids": {"extract": {"config": {"date_from": date_from, "date_to": date_to}}}}