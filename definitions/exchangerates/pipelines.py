from dagster import pipeline

from definitions.exchangerates.solids import extract, load, transform


def load_exchangerates_pipline():
    @pipeline
    def exchangerates_pipline():
        return load(transform(extract()))

    return exchangerates_pipline
