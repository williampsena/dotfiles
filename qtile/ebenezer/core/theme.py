from pathlib import Path
from string import Template

from ebenezer.core.config.settings import AppSettings, AppSettingsColors
from ebenezer.core.dict import merge_dicts_recursive
from ebenezer.core.files import resolve_file_path
from ebenezer.core.yaml import read_yaml_file
from libqtile.log_utils import logger

ROFI_TEMPLATES = [["$rofi_home/_vars.template.rasi", "$rofi_home/_vars.rasi"]]
DUNSTRC_HOME_PATH = "$home/.config/dunst"


def preload_colors(settings: AppSettings) -> AppSettings:
    theme = settings.colors.theme

    if theme:
        settings = _apply_theme_color(theme, settings)

    _apply_rofi_style(settings)
    _apply_dusnt_style(settings)

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


def _apply_rofi_style(settings: AppSettings):
    try:
        colors = {
            "font": f"{settings.fonts.rofi_font} {settings.fonts.rofi_font_size}",
            "background": settings.colors.rofi_background,
            "background_alt": settings.colors.rofi_background_alt,
            "foreground": settings.colors.rofi_foreground,
            "selected": settings.colors.rofi_selected,
            "active": settings.colors.rofi_active,
            "urgent": settings.colors.rofi_urgent,
            "border": settings.colors.rofi_border,
            "border_alt": settings.colors.rofi_border_alt,
            "colors": _extract_rasi_colors(settings.colors),
        }

        for template_file, target_file in ROFI_TEMPLATES:
            with open(resolve_file_path(template_file), "r") as f:
                cmd_template = Template(f.read())
                content = cmd_template.safe_substitute(colors).strip()

                with open(resolve_file_path(target_file), "w") as f:
                    f.write(content)
    except Exception as e:
        logger.warning("error while trying to build rofi style", e, exc_info=True)


def _extract_rasi_colors(colors: AppSettingsColors) -> str:
    colors_list = [
        f"    {color.replace("_", "-")}: {value};"
        for color, value in colors.raw.items()
    ]
    return "\n".join(colors_list)


def _apply_dusnt_style(settings: AppSettings):
    try:
        template_file = resolve_file_path(f"{DUNSTRC_HOME_PATH}/dunstrcbaserc")
        target_file = resolve_file_path(f"{DUNSTRC_HOME_PATH}/dunstrc")

        style = {
            "font": f"{settings.fonts.font_notification} {settings.fonts.font_notification_size}",
            "background": settings.colors.bg_normal,
            "foreground": settings.colors.fg_normal,
            "frame_color": settings.colors.fg_normal,
            "highlight_color": settings.colors.fg_selected,
            "urgency_low_background": settings.colors.bg_normal,
            "urgency_low_foreground": settings.colors.fg_normal,
            "urgency_normal_background": settings.colors.bg_normal,
            "urgency_normal_foreground": settings.colors.fg_normal,
            "urgency_critical_background": settings.colors.bg_urgent,
            "urgency_critical_foreground": settings.colors.fg_urgent,
            "urgency_critical_frame_color": settings.colors.border_color_marked,
        }

        with open(resolve_file_path(template_file), "r") as f:
            cmd_template = Template(f.read())
            content = cmd_template.safe_substitute(style).strip()

            with open(resolve_file_path(target_file), "w") as f:
                f.write(content)
    except Exception as e:
        logger.warning("error while trying to build dusnt style", e, exc_info=True)
