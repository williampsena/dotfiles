import time
from libqtile.log_utils import logger

def request_retry(operation, retries=3, delay=2):
    for attempt in range(retries):
        try:
            result = operation()
            return result
        except Exception as e:
            logger.warn(f"Attempt {attempt + 1} failed: {e}", e, exc_info=True)
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                raise 
