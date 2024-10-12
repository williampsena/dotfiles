import subprocess
from string import Template
from ebenezer.core.files import resolve_file_path


def build_shell_command(raw_cmd: str, **kwargs: object) -> str:
    cmd_template = Template(resolve_file_path(raw_cmd))

    return cmd_template.safe_substitute(kwargs).strip()


def run_shell_command(raw_cmd: str, **kwargs: object) -> subprocess.CompletedProcess:
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
