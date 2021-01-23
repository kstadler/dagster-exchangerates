from dagster import EventMetadataEntry
from dagster_pandas import PandasColumn, create_dagster_pandas_dataframe_type


def compute_exchange_rate_dataframe_summary_statistics(dataframe):
    return [
        EventMetadataEntry.text(
            min(dataframe["day"]),
            "min_day",
            "Minimum date of exchange rates",
        ),
        EventMetadataEntry.text(
            max(dataframe["day"]),
            "max_day",
            "Maximum date of exchange rates",
        ),
        EventMetadataEntry.text(
            str(dataframe["day"].nunique()),
            "num_unique_day",
            "Total unique dates of exchange rates",
        ),
        EventMetadataEntry.text(
            str(dataframe["currency"].nunique()),
            "num_unique_currency",
            "Total unique currencies of exchange rates",
        ),
        EventMetadataEntry.text(
            str(len(dataframe)), "n_rows", "Number of rows seen in the dataframe"
        ),
    ]


ExchangeRateDataFrame = create_dagster_pandas_dataframe_type(
    name="ExchangeRateDataFrame",
    columns=[
        PandasColumn.string_column("id"),
        PandasColumn.string_column("day"),
        PandasColumn.string_column("currency"),
        PandasColumn.numeric_column("rate"),
    ],
    event_metadata_fn=compute_exchange_rate_dataframe_summary_statistics
)
