from os import listdir
from pathlib import Path
import json


def get_filenames(directory: Path):
    files = []
    for f in directory.iterdir():
        files.append(f)
    return files


def valid_json(json_data):
    try:
        json.load(json_data)
    except ValueError:
        return False
    return True


def valid_file(filename: str):
    with open(filename, 'r') as file:
        if valid_json(file):
            return True


def get_valid_json_files():
    current_path = Path.cwd()

    json_dir = current_path / 'event'
    json_files = get_filenames(json_dir)
    json_files = list(filter(lambda filename: valid_file(filename), json_files))

    schema_dir = current_path / 'schema'
    schema_files = get_filenames(schema_dir)
    schema_files = list(filter(lambda filename: valid_file(filename), schema_files))

    return json_files, schema_files
