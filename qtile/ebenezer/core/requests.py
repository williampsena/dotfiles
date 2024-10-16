import time
from libqtile.log_utils import logger


def request_retry(operation, retries=5, delay=2):
    for attempt in range(retries):
        try:
            return operation()
        except Exception as e:
            logger.warn(f"Attempt {attempt + 1} failed: {e}", e, exc_info=True)
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                raise
