from pathlib import Path

import yaml

TEST_CONFIG = Path("config.test.yml")


def load_raw_test_settings():
    return load_raw_settings(str(TEST_CONFIG))


def load_raw_settings(
    config_filepath=None, colors_filepath=None, applications_filepath=None
):
    return merge_yaml([config_filepath, colors_filepath, applications_filepath])


def merge_yaml(file_paths):
    merged_data = {}

    for file_path in file_paths:
        if file_path:
            data = _read_yaml_file(file_path)
            merged_data.update(data)

    return merged_data


def _read_yaml_file(filepath: str):
    with open(filepath, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)
