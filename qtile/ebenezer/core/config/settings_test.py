from ebenezer.core.config.colors import AppSettingsColors
from ebenezer.core.config.environment import AppSettingsEnvironment
from ebenezer.core.config.fonts import AppSettingsFonts
from ebenezer.core.config.loader import TEST_CONFIG, load_raw_test_settings
from ebenezer.core.config.lock_screen import AppSettingsLockScreen
from ebenezer.core.config.monitoring import AppSettingsMonitoring
from ebenezer.core.config.settings import AppSettings, load_settings


def test_parse_settings():
    raw_settings = load_raw_test_settings()
    settings = load_settings(TEST_CONFIG)
    expected = AppSettings(
        environment=AppSettingsEnvironment(
            mod="mod4",
            browser="firefox",
            terminal="kitty",
            wallpaper_dir="/home/foo/wallpapers",
            wallpaper_timeout="60",
            os_logo="/home/foo/logos/linux.svg",
            os_logo_icon="󰌽",
            os_logo_icon_color="#6200EA",
            theme="ebenezer",
            backlight_name="",
            weather_api_key="foo",
            city_id="1",
        ),
        fonts=AppSettingsFonts(
            font="Fira Code Nerd Font Bold",
            font_regular="Fira Code Nerd Font Medium",
            font_light="Fira Code Nerd Font Light",
            font_strong="Fira Code Nerd Font Semibold",
            font_strong_bold="Fira Code Nerd Font Bold",
            font_size=14,
            font_icon="Fira Code Nerd Font Medium",
            font_icon_size=16,
        ),
        groups={
            "browsers": "",
            "terminal": "",
            "editors": "󰘐",
            "games": "",
            "files": "󰉋",
            "win": "󰍲",
        },
        groups_layout={"default": "monadtall", "win": "tile"},
        startup={
            "keyboard_layout": "setxkbmap -model abnt2 -layout br && localectl set-x11-keymap br",
            "dunst": "pkill dunst && dunst &",
        },
        floating={
            "title": [],
            "wm_class": [
                "pavucontrol",
                "gnome-calculator",
            ],
        },
        colors=AppSettingsColors(
            fg_normal="#D8DEE9",
            fg_focus="#C4C7C5",
            fg_urgent="#CC9393",
            bg_normal="#263238",
            bg_focus="#1E2320",
            bg_urgent="#424242",
            bg_systray="#37444b",
            bg_selected="#5c6b73",
            fg_blue="#304FFE",
            fg_ligth_blue="#B3E5FC",
            fg_yellow="#FFFF00",
            fg_red="#D50000",
            fg_orange="#FFC107",
            fg_purple="#AA00FF",
            fg_green="#4BC1CC",
            fg_gray="#9db4c0",
            bg_topbar="#282a36",
            bg_topbar_arrow="#5c6b73",
            bg_topbar_selected="#6200EA",
            border_color_normal="#AA00FF",
            border_color_active="#6200EA",
            border_color_marked="#c678dd",
            titlebar_bg_focus="#263238",
            titlebar_bg_normal="#253238",
            taglist_bg_focus="#37474F",
            group_focus="#e0fbfc",
            group_normal="#C4C7C5",
        ),
        commands={
            "screenshot": "flameshot gui --clipboard --path ~/Pictures/Screenshots",
            "screenshot_full": "flameshot full --clipboard --path ~/Pictures/Screenshots",
            "change_wallpaper": "echo 'change wallpaper'",
        },
        lock_screen=AppSettingsLockScreen(
            command="~/.config/qtile/lock.py",
            timeout=10,
            font="Mononoki Nerd Font Bold",
            font_size=40,
            joke_font_path="/usr/share/fonts/TTF/MononokiNerdFont-Regular.ttf",
            joke_font_size=17,
            joke_providers="reddit,icanhazdad",
            joke_foreground_color="#000",
            joke_text_color="#fff",
            icanhazdad_joke_url="https://icanhazdadjoke.com/",
            reddit_joke_url="https://www.reddit.com/r/ProgrammerDadJokes.json",
            blurtype="0x7",
            blank_color="#00000000",
            clear_color="#ffffff22",
            default_color="#9db4c0",
            key_color="#8a8ea800",
            text_color="#4BC1CC",
            wrong_color="#D50000",
            verifying_color="#41445800",
        ),
        monitoring=AppSettingsMonitoring(
            default_color="fg_normal",
            high_color="fg_orange",
            medium_color="fg_yellow",
            threshold_medium=70,
            threshold_high=90,
            burn=True,
        ),
    )

    assert settings.environment.__dict__ == expected.environment.__dict__
    assert settings.fonts.__dict__ == expected.fonts.__dict__
    assert settings.groups == expected.groups
    assert settings.groups_layout == expected.groups_layout
    assert settings.startup == expected.startup
    assert settings.floating == expected.floating
    assert settings.colors.__dict__ == expected.colors.__dict__
    assert settings.commands == expected.commands
    assert settings.lock_screen.__dict__ == expected.lock_screen.__dict__
    assert settings.monitoring.__dict__ == expected.monitoring.__dict__
