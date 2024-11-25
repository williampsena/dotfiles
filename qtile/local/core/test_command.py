from local.core.command import build_shell_command
from local.core.files import qtile_home


def test_build_shell_command():
    raw_commands = [
        'xautolock -detectsleep -time $timeout -locker "python $qtile_home/lock.py" &',
        "$qtile_home/ebenezer/scripts/wallpaper.sh slideshow $wallpaper_dir $wallpaper_timeout &",
    ]
    expectations = [
        f'xautolock -detectsleep -time 10 -locker "python {qtile_home}/lock.py" &',
        f"{qtile_home}/ebenezer/scripts/wallpaper.sh slideshow /wallpapers 30 &",
    ]

    for i, raw_cmd in enumerate(raw_commands):
        cmd = build_shell_command(
            raw_cmd, timeout=10, wallpaper_dir="/wallpapers", wallpaper_timeout=30
        )
        assert cmd == expectations[i]

        cmd = build_shell_command(
            raw_cmd,
            **{"timeout": 10, "wallpaper_dir": "/wallpapers", "wallpaper_timeout": 30},
        )
        assert cmd == expectations[i]
