from dagster import pipeline

from .solids import extract, load, transform


@pipeline
def exchangerates_pipline():
    load(transform(extract()))
