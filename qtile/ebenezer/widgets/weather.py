from libqtile import widget
from ebenezer.core.config.settings import AppSettings


def build_weather_widget(settings: AppSettings, kwargs: dict):
    default_args = {
        "font": settings.fonts.font_icon,
        "fontsize": settings.fonts.font_icon_size,
        "padding": 2,
        "cityid": settings.environment.city_id,
        "app_key": settings.environment.weather_api_key,
        "location": "London",
        "format": "{icon}",
    }

    args = default_args | kwargs

    return widget.OpenWeather(**args)
