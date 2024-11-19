from ebenezer.core.config.colors import AppSettingsColors
from ebenezer.core.config.loader import load_raw_test_settings


def test_parse_colors():
    settings = load_raw_test_settings()
    colors = AppSettingsColors(**settings.get("colors"))
    expected = AppSettingsColors(
        fg_normal="#D8DEE9",
        fg_focus="#C4C7C5",
        fg_urgent="#CC9393",
        bg_normal="#263238",
        bg_focus="#1E2320",
        bg_urgent="#424242",
        bg_systray="#37444b",
        bg_selected="#5c6b73",
        fg_blue="#304FFE",
        fg_light_blue="#B3E5FC",
        fg_yellow="#FFFF00",
        fg_red="#D50000",
        fg_orange="#FFC107",
        fg_purple="#AA00FF",
        fg_green="#4BC1CC",
        fg_gray="#9db4c0",
        fg_white="#ffffff",
        fg_black="#000000",
        fg_selected="#AA00FF",
        bg_topbar="#282a36",
        bg_topbar_selected="#6200EA",
        bg_topbar_arrow="#5c6b73",
        border_color_normal="#AA00FF",
        border_color_active="#6200EA",
        border_color_marked="#c678dd",
        titlebar_bg_focus="#263238",
        titlebar_bg_normal="#253238",
        taglist_bg_focus="#37474F",
        group_focus="#e0fbfc",
        group_normal="#C4C7C5",
        lock_screen_blank_color="#00000000",
        lock_screen_clear_color="#ffffff22",
        lock_screen_default_color="#9db4c0",
        lock_screen_key_color="#8a8ea800",
        lock_screen_text_color="#4BC1CC",
        lock_screen_wrong_color="#D50000",
        lock_screen_verifying_color="#41445800",
        lock_screen_joke_foreground_color="#000",
        lock_screen_joke_text_color="#fff",
    )

    assert colors.__dict__ == expected.__dict__


def test_get_color():
    settings = load_raw_test_settings()
    colors = AppSettingsColors(**settings.get("colors"))

    assert colors.get_color("#000") == "#000"
    assert colors.get_color("fg_yellow") == "#FFFF00"
    assert colors.get_color("foo_bar") == "#D8DEE9"
