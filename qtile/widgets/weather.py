from libqtile import widget
from settings import AppSettings


def build_weather_widget(settings: AppSettings):
    return widget.OpenWeather(
        font=settings.fonts.font_icon,
        fontsize=settings.fonts.font_icon_size,
        padding=2,
        cityid=settings.environment.city_id,
        app_key=settings.environment.weather_api_key,
        location="London",
        format="{location_city}: {icon}",
    )
