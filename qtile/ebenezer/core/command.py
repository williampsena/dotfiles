import subprocess
from string import Template
from typing import Optional

from ebenezer.core.files import resolve_file_path
from libqtile.lazy import lazy

DEFAULT_TIMEOUT = 10


def build_shell_command(raw_cmd: str, **kwargs: object) -> str:
    cmd_template = Template(resolve_file_path(raw_cmd))

    return cmd_template.safe_substitute(kwargs).strip()


def run_shell_command(
    raw_cmd: str, timeout: Optional[float] = 10, **kwargs: object
) -> subprocess.CompletedProcess:
    return subprocess.run(
        build_shell_command(raw_cmd, **kwargs),
        shell=True,
    )


def run_shell_command_stdout(
    raw_cmd: str, **kwargs: object
) -> subprocess.CompletedProcess:
    return subprocess.run(
        build_shell_command(raw_cmd, **kwargs),
        shell=True,
        stdout=subprocess.PIPE,
        text=True,
    )


def lazy_command(cmd: str | None, **kwargs: object):
    @lazy.function
    def _inner(qtile):
        if cmd is None:
            return

        return run_shell_command(build_shell_command(cmd, **kwargs))

    return _inner


def lazy_spawn(cmd: str, **kwargs: object):
    return lazy.spawn(build_shell_command(cmd, **kwargs))
