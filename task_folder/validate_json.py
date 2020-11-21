from jsonschema import validate, exceptions
from os import sep as os_sep
from validate_source import get_valid_json_files
from write_log import logger
import json

json_files, schema_files = get_valid_json_files()


def json_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)


def validate_json():
    for s in schema_files:
        for j in json_files:
            s_name = str(s).split(os_sep)[-1]
            j_name = str(j).split(os_sep)[-1]

            try:
                validate(instance=json_data(j), schema=json_data(s))
                result = f'Validation passed for {j_name} with schema {s_name}'
            except exceptions.ValidationError as err:
                result = f'Error occured while validating {j_name} with schema {s_name}; {err.message}'

            logger.info(result)


if __name__ == '__main__':
    validate_json()
