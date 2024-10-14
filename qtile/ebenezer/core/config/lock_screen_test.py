from ebenezer.core.config.loader import load_raw_test_settings
from ebenezer.core.config.lock_screen import AppSettingsLockScreen


def test_parse_lock_screen():
    settings = load_raw_test_settings()
    lock_screen = AppSettingsLockScreen(**settings.get("lock_screen"))
    expected = AppSettingsLockScreen(
        command="~/.config/qtile/lock.py",
        timeout=10,
        font="/usr/share/fonts/TTF/MononokiNerdFont-Regular.ttf",
        font_size=17,
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
    )

    assert lock_screen.__dict__ == expected.__dict__
