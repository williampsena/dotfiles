from ebenezer.core.config.settings import AppSettings
from libqtile import widget


def build_weather_widget(settings: AppSettings, kwargs: dict):
    default_args = {
        "font": settings.fonts.font_icon,
        "fontsize": settings.fonts.font_icon_size,
        "foreground": settings.colors.fg_normal,
        "padding": 2,
        "cityid": settings.environment.city_id,
        "app_key": settings.environment.weather_api_key,
        "location": "London",
        "format": "{icon}",
    }

    args = default_args | kwargs

    return widget.OpenWeather(**args)
