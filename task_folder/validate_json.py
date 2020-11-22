from jsonschema import validate, exceptions, Draft7Validator
from os import sep as os_sep
from validate_source import get_valid_json_files
from write_log import logger
import json


def json_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)


def validate_json():
    '''
    sends errors with paths/names of validating files
    to log_error function if there is validation error
    '''
    json_files, schema_files = get_valid_json_files()
    row = 0
    for s_filepath in schema_files:
        validator = Draft7Validator(json_data(s_filepath))

        for j_filepath in json_files:
            errors = validator.iter_errors(json_data(j_filepath))

            if errors:
                log_error(row, s_filepath, j_filepath, errors)
                row += 1


def log_error(row, s_filepath, j_filepath, errors):
    '''
    write error to log file
    '''
    s_filename = str(s_filepath).split(os_sep)[-1]
    j_filename = str(j_filepath).split(os_sep)[-1]
    result = f'{row}. Error occured while validating {j_filename} with schema {s_filename};'
    for error in errors:
        result += f'<br>__{error.message}__<br>'

    logger.info(result)


if __name__ == '__main__':
    validate_json()
