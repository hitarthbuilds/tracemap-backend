import signal


class ExecutionTimeout(Exception):
    """Raised when traced code exceeds execution time limit."""
    pass


def _timeout_handler(signum, frame):
    raise ExecutionTimeout("Execution time limit exceeded")


def run_with_timeout(fn, seconds: int = 2):
    """
    Run a function with a hard execution time limit.
    """
    signal.signal(signal.SIGALRM, _timeout_handler)
    signal.alarm(seconds)
    try:
        return fn()
    finally:
        signal.alarm(0)
