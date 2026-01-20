from tracemap.api import trace
from tracemap.export.snapshot import export_snapshot
from app.guards.limits import run_with_timeout
from app.services.jobs import (
    create_job,
    set_running,
    set_result,
    set_error,
    executor,
)
def trace_code(code: str) -> dict:
    """
    Execute and trace Python code using TraceMap engine.
    """

    def _run():
        graph = trace(code)
        return export_snapshot(graph)

    return run_with_timeout(_run)


def trace_code_sync(code: str) -> dict:
    def _run():
        graph = trace(code)
        return export_snapshot(graph)

    return run_with_timeout(_run)


def trace_code_async(code: str) -> str:
    job_id = create_job()

    def task():
        try:
            set_running(job_id)
            result = trace_code_sync(code)
            set_result(job_id, result)
        except Exception as e:
            set_error(job_id, str(e))

    executor.submit(task)
    return job_id