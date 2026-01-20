from tracemap.api import trace
from tracemap.export.snapshot import export_snapshot
from app.guards.limits import run_with_timeout


def trace_code(code: str) -> dict:
    """
    Execute and trace Python code using TraceMap engine.
    """

    def _run():
        graph = trace(code)
        return export_snapshot(graph)

    return run_with_timeout(_run)
