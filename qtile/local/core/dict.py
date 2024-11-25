def merge_dicts_recursive(base: dict, override: dict):
    for key, value in override.items():
        if key in base and isinstance(base[key], dict) and isinstance(value, dict):
            merge_dicts_recursive(base[key], value)
        else:
            base[key] = value
    return base
