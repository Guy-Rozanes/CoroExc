import functools
import time

# 404 status code is only for testing my retry
STATUS_CODES_TO_RETRY = [500, 502, 503, 404]


def retry_on_server_error(max_retries=3, retry_interval=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    response = func(*args, **kwargs)
                    if response.status_code in STATUS_CODES_TO_RETRY:
                        print("Server returned 500 error. Retrying...")
                        retries += 1
                        time.sleep(retry_interval)
                    else:
                        return response
                except Exception as e:
                    print(e)
            raise RuntimeError(f"Max retries reached. Last response: {response.status_code}")

        return wrapper

    return decorator
