#!/usr/bin/env python3

from libqtile.command import Client


def run():
    client = Client()
    client.shutdown()


if __name__ == "__main__":
    run()
