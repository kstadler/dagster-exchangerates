import requests
from dagster import solid, Output, Field, OutputDefinition, InputDefinition
from pandas import DataFrame
import sqlite3

from definitions.exchangerates.dagster_types import ExchangeRateDataFrame


@solid(
    config_schema={
        "base_currency": Field(str, is_required=False, default_value="EUR"),
        "date_from": str,
        "date_to": str,
    }
)
def extract(context):
    result = requests.get(
        f"https://api.exchangeratesapi.io/history?"
        f"&start_at={context.solid_config['date_from']}"
        f"&end_at={context.solid_config['date_to']}"
        f"&base={context.solid_config['base_currency']}"
    )
    if result.status_code != 200:
        raise ValueError("API didn't return valid result")
    return result.json()


@solid(output_defs=[OutputDefinition(ExchangeRateDataFrame)])
def transform(context, currency_json) -> DataFrame:
    data = []
    for day in currency_json["rates"]:
        for currency in currency_json["rates"][day]:
            data.append(
                {
                    "id": f"{day}-{currency}",
                    "day": day,
                    "currency": currency,
                    "rate": currency_json["rates"][day][currency],
                }
            )

    yield Output(DataFrame(data))


@solid(input_defs=[InputDefinition(name="df", dagster_type=ExchangeRateDataFrame)])
def load(context, df: DataFrame):
    sql_create_table = """create table if not exists exchangerates (
                        id text primary key,
                        day text,
                        currency text,
                        rate decimal(32,4)
                    );"""

    sql_update = """update exchangerates
                    set day      = (select day from stage where exchangerates.id = stage.id),
                        currency = (select stage.currency from stage where exchangerates.id = stage.id),
                        rate     = (select rate from stage where exchangerates.id = stage.id)
                    where exchangerates.id in (select id from stage);
                    """

    sql_insert = """insert into exchangerates (id, day, currency, rate)
                    select id, day, currency, rate
                    from stage s
                    where not exists
                        (select 1
                         from exchangerates e
                         where e.id = s.id);"""

    conn = sqlite3.connect("exchangerates.sqlite")
    conn.execute(sql_create_table)
    df.to_sql("stage", conn, if_exists="replace")
    conn.execute(sql_update)
    conn.execute(sql_insert)
    conn.commit()
