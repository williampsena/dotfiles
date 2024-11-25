import yaml


def read_yaml_file(filepath: str) -> dict:
    with open(filepath, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)
