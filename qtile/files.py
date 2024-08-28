from pathlib import Path

home = str(Path.home())
qtile_home = str(Path.joinpath(Path(home), ".config/qtile"))
theme_home = str(Path.joinpath(Path(qtile_home), "themes"))


def resolve_file_path(path: str) -> str:
    return (
        path.replace("$HOME", home)
        .replace("$QTILE_HOME", qtile_home)
        .replace("$THEME", theme_home)
    )
