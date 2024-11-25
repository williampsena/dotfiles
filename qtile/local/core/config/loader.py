from local.core.dict import merge_dicts_recursive
from local.core.yaml import read_yaml_file

TEST_CONFIG = "config.test.yml"
TEST_COLOR_CONFIG = "colors.test.yml"


def load_raw_test_settings():
    return load_raw_settings(
        config_filepath=TEST_CONFIG, colors_filepath=TEST_COLOR_CONFIG
    )


def load_raw_settings(
    config_filepath=None,
    colors_filepath=None,
    applications_filepath=None,
    keybindings_filepath=None,
) -> dict:
    return merge_yaml(
        [colors_filepath, applications_filepath, keybindings_filepath, config_filepath]
    )


def merge_yaml(file_paths, merged_data: dict = {}) -> dict:
    for file_path in file_paths:
        if file_path:
            data = read_yaml_file(file_path)
            merged_data = merge_dicts_recursive(merged_data, data)

    return merged_data
