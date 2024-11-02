from pathlib import Path

from libqtile.log_utils import logger

from ebenezer.core.config.settings import AppSettings, AppSettingsColors
from ebenezer.core.dict import merge_dicts_recursive
from ebenezer.core.files import resolve_file_path
from ebenezer.core.yaml import read_yaml_file


def preload_colors(settings: AppSettings) -> AppSettings:
    theme = settings.colors.theme

    if theme:
        settings = _apply_theme_color(theme, settings)

    return settings


def _apply_theme_color(theme_filepath: str, settings: AppSettings) -> AppSettings:
    try:
        theme_filepath = resolve_file_path(theme_filepath)

        if not Path(theme_filepath).exists():
            logger.warning(f"Not found the selected theme {theme_filepath}.")
            return settings

        theme_config = read_yaml_file(resolve_file_path(theme_filepath))

        args = merge_dicts_recursive(
            settings.colors.raw, theme_config.get("colors", {})
        )

        settings.colors = AppSettingsColors(**args)

        return settings
    except Exception as e:
        logger.warning("error while trying to apply selected theme", e, exc_info=True)
        return settings
