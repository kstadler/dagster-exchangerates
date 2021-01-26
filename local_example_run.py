from dagster import execute_pipeline

from definitions.exchangerates.pipelines import load_exchangerates_pipline

execute_pipeline(load_exchangerates_pipline(), run_config={"solids": {"extract": {"config": {"date_from": "2020-01-01", "date_to": "2020-12-31"}}}})