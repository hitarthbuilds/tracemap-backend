from concurrent.futures import ThreadPoolExecutor, TimeoutError


class ExecutionTimeout(Exception):
    """Raised when traced code exceeds execution time limit."""
    pass


def run_with_timeout(fn, seconds: int = 2):
    """
    Run a function with a hard execution time limit.
    Thread-safe. Works inside FastAPI.
    """
    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(fn)
        try:
            return future.result(timeout=seconds)
        except TimeoutError:
            raise ExecutionTimeout("Execution time limit exceeded")
