from pathlib import Path
from string import Template

home = str(Path.home())
qtile_home = str(Path.joinpath(Path(home), ".config/qtile"))
theme_home = str(Path.joinpath(Path(qtile_home), "themes"))
rofi_home = str(Path.joinpath(Path(qtile_home), "ebenezer/rofi"))
scripts = str(Path.joinpath(Path(qtile_home), "ebenezer/scripts"))


def resolve_file_path(raw_path: str) -> str:
    cmd_template = Template(raw_path)
    return cmd_template.safe_substitute(
        home=home,
        qtile_home=qtile_home,
        theme=theme_home,
        theme_home=theme_home,
        rofi_home=rofi_home,
        scripts=scripts,
    ).strip()
