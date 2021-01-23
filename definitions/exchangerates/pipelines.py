from dagster import pipeline

from definitions.exchangerates.solids import extract, load, transform


@pipeline
def exchangerates_pipline():
    load(transform(extract()))
