import uuid
from concurrent.futures import ThreadPoolExecutor
from typing import Dict, Any

# Simple in-memory job store
JOBS: Dict[str, Dict[str, Any]] = {}

executor = ThreadPoolExecutor(max_workers=4)


def create_job() -> str:
    job_id = str(uuid.uuid4())
    JOBS[job_id] = {"status": "pending", "result": None, "error": None}
    return job_id


def set_running(job_id: str):
    JOBS[job_id]["status"] = "running"


def set_result(job_id: str, result: dict):
    JOBS[job_id]["status"] = "done"
    JOBS[job_id]["result"] = result


def set_error(job_id: str, error: str):
    JOBS[job_id]["status"] = "error"
    JOBS[job_id]["error"] = error


def get_job(job_id: str):
    return JOBS.get(job_id)
