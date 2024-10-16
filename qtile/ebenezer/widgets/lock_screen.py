import random
import re
import subprocess
import requests
import os
import psutil
from string import Template
from pathlib import Path
from typing import List, Callable
from PIL import Image, ImageDraw, ImageFont
from libqtile.log_utils import logger
from libqtile import widget
from libqtile import qtile
from libqtile.lazy import lazy
from ebenezer.core.config.settings import AppSettings, load_settings
from ebenezer.core.files import resolve_file_path
from ebenezer.core.requests import request_retry

OUTPUT_FILE = "/tmp/i3lock.png"
JOKE_OUTPUT_FILE = "/tmp/joke.png"


def __is_i3lock_running__():
    try:
        subprocess.check_output(["pgrep", "i3lock"])
        return True
    except subprocess.CalledProcessError:
        return False


def __remove_emojis__(text):
    emoji_pattern = re.compile(
        "["  # Start of character class
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F700-\U0001F77F"  # alchemical symbols
        "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
        "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
        "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        "\U0001FA00-\U0001FA6F"  # Chess Symbols
        "\U00002700-\U000027BF"  # Dingbats
        "\u2600-\u26FF"  # Misc symbols
        "\u2700-\u27BF"  # Dingbats
        "\u2B50"  # Star
        "]+",
        flags=re.UNICODE,
    )

    return emoji_pattern.sub(r"", text)


def __get_joke_from_icanhazdadjoke__(settings: AppSettings) -> Callable[[], str]:
    def do_request():
        headers = {"Accept": "application/json"}
        return requests.get(settings.lock_screen.icanhazdad_joke_url, headers=headers)

    def inner():
        response = request_retry(do_request)

        if response.status_code == requests.codes.ok:
            return __remove_emojis__(response.json()["joke"])
        else:
            return "Something went wrong: {}".format(response.status_code)

    return inner


def __get_joke_from_reddit__(settings: AppSettings) -> Callable[[], str]:
    def do_request():
        headers = {"Accept": "application/json"}
        return requests.get(settings.lock_screen.reddit_joke_url).json()

    def inner():
        data = request_retry(do_request)

        jokes = data.get("data").get("children") or []
        joke = random.choice(jokes)
        data = joke.get("data")

        punchline = re.sub("&amp;#x200B;", "", __remove_emojis__(data.get("selftext")))

        return f"{__remove_emojis__(data.get("title"))}\n{punchline}"

    return inner


def __load_joke_providers__(settings: AppSettings):
    return {
        "reddit": __get_joke_from_reddit__(settings),
        "icanhazdad": __get_joke_from_icanhazdadjoke__(settings),
    }


def __get_joke__(settings: AppSettings) -> str:
    joke_providers = __load_joke_providers__(settings)
    joke_providers_selected = [
        key for key in settings.lock_screen.joke_providers if key in joke_providers
    ]
    random.shuffle(joke_providers_selected)

    for joke_provider_key in joke_providers_selected:
        try:
            return joke_providers[joke_provider_key]()
        except Exception as e:
            logger.warning(
                f"error while trying to fetch jokes from {joke_provider_key}",
                e,
                exc_info=True,
            )
            next

    return "No jokes!"


def __remove_output_files__():
    for raw_filepath in [OUTPUT_FILE, JOKE_OUTPUT_FILE]:
        file_path = Path(raw_filepath)

        if file_path.exists():
            file_path.unlink()


def __build_joke_image__(settings: AppSettings, joke: str, width: int, height: int):
    img = Image.new(
        "RGB", (width, height), color=settings.lock_screen.joke_foreground_color
    )
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype(settings.lock_screen.font, settings.lock_screen.font_size)

    bbox = draw.textbbox((0, 0), joke, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    position = ((width - text_width) // 2, ((height - text_height) // 2) * 0.2)

    draw.text(
        position,
        joke,
        font=font,
        fill=settings.lock_screen.joke_text_color,
    )

    img.save(JOKE_OUTPUT_FILE)


def __build_background__(settings: AppSettings):
    background = Image.open(OUTPUT_FILE)
    width, height = background.size

    joke = __get_joke__(settings)
    __build_joke_image__(settings, joke=joke, width=width, height=height)

    overlay = Image.open(JOKE_OUTPUT_FILE)

    background = background.convert("RGBA")
    overlay = overlay.convert("RGBA")

    new_img = Image.blend(background, overlay, 0.5)
    new_img.save(OUTPUT_FILE, "PNG")


def __run_command__(commands: List[List[str]]):
    for cmd in commands:
        command = subprocess.Popen(cmd)
        command.wait()


def __prepare_lock_screen__(settings: AppSettings):
    __remove_output_files__()

    __run_command__(
        [
            ["scrot", OUTPUT_FILE],
            [
                "magick",
                "convert",
                "-blur",
                settings.lock_screen.blurtype,
                OUTPUT_FILE,
                OUTPUT_FILE,
            ],
        ]
    )

    __build_background__(settings)


def lock_screen(settings: AppSettings):
    if __is_i3lock_running__():
        logger.warning("i3lock already running")
        return

    __run_command__([["notify-send", "󰌾 locking screen..."]])
    __prepare_lock_screen__(settings)
    run_i3_lock(settings)


def run_i3_lock(settings: AppSettings):
    cmd_template = Template(
        """
    i3lock
    --nofork
    -i
    $image
    --insidever-color=$clear
    --ringver-color=$verifying
    --insidewrong-color=$wrong
    --ringwrong-color=$default
    --inside-color=$clear
    --ring-color=$default
    --line-color=$blank
    --separator-color=$default
    --verif-color=$text
    --wrong-color=$text
    --time-color=$text
    --date-color=$text
    --layout-color=$text
    --keyhl-color=$key
    --bshl-color=$wrong
    --indicator
    --clock
    --time-str=%H:%M
    """
    )

    cmd_options = cmd_template.substitute(
        image=OUTPUT_FILE,
        blurtype=settings.lock_screen.blurtype,
        blank=settings.lock_screen.blank_color,
        clear=settings.lock_screen.clear_color,
        default=settings.lock_screen.default_color,
        key=settings.lock_screen.key_color,
        text=settings.lock_screen.text_color,
        wrong=settings.lock_screen.wrong_color,
        verifying=settings.lock_screen.verifying_color,
    ).strip()

    cmd_options = re.sub(r"\s+", " ", cmd_options)

    __run_command__([cmd_options.split(" ")])


def click_lock_screen(settings: AppSettings):
    def inner():
        try:
            lock_screen(settings)
        except Exception as e:
            logger.warning(
                "error while trying to run lock screen widget", e, exc_info=True
            )

    return inner


def build_lock_screen_widget(settings: AppSettings):
    return widget.TextBox(
        " ",
        font=settings.fonts.font_icon,
        fontsize=settings.fonts.font_icon_size,
        padding=2,
        foreground=settings.colors.fg_normal,
        mouse_callbacks={"Button1": click_lock_screen(settings)},
    )
