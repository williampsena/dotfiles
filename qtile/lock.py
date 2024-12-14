#!/usr/bin/env python3

from ebenezer.config.settings import load_settings_by_files
from local.core.theme import preload_colors
from ebenezer.widgets.lock_screen import lock_screen


def run():
    settings = load_settings_by_files()
    settings = preload_colors(settings)
    lock_screen(settings)


if __name__ == "__main__":
    run()
