from datetime import date

from dagster import execute_solid

from definitions.solids import extract


def is_key_in_dict(dict, key):
    for element in dict:
        if key in element:
            return True


def test_extract_solid():
    date_from = date(year=2010, month=1, day=1).isoformat()
    date_to = date(year=2010, month=12, day=31).isoformat()
    run_config = {"solids": {"extract": {"config": {"date_from": date_from, "date_to": date_to}}}}
    result = execute_solid(extract, run_config=run_config)
    output = result.output_values['result']

    assert 'rates' in output
    assert len(output['rates']) > 250
    assert is_key_in_dict(output['rates'], '2010-01-04')
    assert is_key_in_dict(output['rates']['2010-01-04'], 'USD')

