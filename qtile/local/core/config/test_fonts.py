from local.core.config.fonts import AppSettingsFonts
from local.core.config.loader import load_raw_test_settings


def test_parse_fonts():
    settings = load_raw_test_settings()
    fonts = AppSettingsFonts(**settings.get("fonts"))
    expected = AppSettingsFonts(
        font="Fira Code Nerd Font Bold",
        font_regular="Fira Code Nerd Font Medium",
        font_light="Fira Code Nerd Font Light",
        font_strong="Fira Code Nerd Font Semibold",
        font_strong_bold="Fira Code Nerd Font Bold",
        font_size=14,
        font_icon="Fira Code Nerd Font Medium",
        font_icon_size=16,
    )

    assert fonts.__dict__ == expected.__dict__
