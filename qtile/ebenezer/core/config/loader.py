from pathlib import Path

import yaml

TEST_CONFIG = Path("config.test.yml")


def load_raw_test_settings():
    return load_raw_settings(str(TEST_CONFIG))


def load_raw_settings(filepath: str):
    with open(filepath, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)
