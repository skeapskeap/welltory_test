
from jsonschema import Draft7Validator
from jsonschema import exceptions as exc
from os import listdir
from pathlib import Path
from write_log import logger
import json


def get_filenames(directory: Path):
    files = []
    for f in directory.iterdir():
        files.append(f)
    return files


def valid_json(filename: str):
    with open(filename, 'r') as json_file:
        try:
            json.load(json_file)
            return True
        except ValueError:
            error = f'Invalid JSON file {filename}<br>'
            logger.info(error)
            return False


def valid_schema(filename: str):
    with open(filename, 'r') as schema_file:
        if valid_json(filename):
            try:
                schema = json.load(schema_file)
                Draft7Validator.check_schema(schema)
                return True
            except exc.SchemaError:
                error = f'Invalid schema file {filename}<br>'
                logger.info(error)
                return False


def get_valid_files():
    '''
    returns filenames with abs path
    '''
    current_path = Path.cwd()

    json_dir = current_path / 'event'
    json_files = get_filenames(json_dir)
    json_files = list(filter(lambda filename: valid_json(filename), json_files))

    schema_dir = current_path / 'schema'
    schema_files = get_filenames(schema_dir)
    schema_files = list(filter(lambda filename: valid_schema(filename), schema_files))

    return json_files, schema_files
