from ebenezer.core.config.loader import load_raw_test_settings
from ebenezer.core.config.lock_screen import AppSettingsLockScreen


def test_parse_lock_screen():
    settings = load_raw_test_settings()
    lock_screen = AppSettingsLockScreen(**settings.get("lock_screen"))
    expected = AppSettingsLockScreen(
        command="~/.config/qtile/lock.py",
        timeout=10,
        font="Mononoki Nerd Font Bold",
        font_size=40,
        joke_font_path="/usr/share/fonts/TTF/MononokiNerdFont-Regular.ttf",
        joke_font_size=17,
        joke_providers="reddit,icanhazdad",
        icanhazdad_joke_url="https://icanhazdadjoke.com/",
        reddit_joke_url="https://www.reddit.com/r/ProgrammerDadJokes.json",
        blurtype="0x7",
    )

    assert lock_screen.__dict__ == expected.__dict__
