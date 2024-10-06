#!/usr/bin/env python3

from ebenezer.core.settings import load_settings
from ebenezer.widgets.lock_screen import lock_screen


def run():
    settings = load_settings()
    lock_screen(settings)


if __name__ == "__main__":
    run()
