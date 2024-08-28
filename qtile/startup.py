import subprocess
from settings import AppSettings
from libqtile.log_utils import logger
from files import resolve_file_path


def run(settings: AppSettings):
    logger.warning(f"loading startup script")
    for cmd in settings.startup:
        try:
            subprocess.run(resolve_file_path(settings.startup[cmd]), shell=True)
            logger.warning(f"the script {cmd} was loaded")
        except:
            logger.warning(f"error while trying to run command {cmd}")
