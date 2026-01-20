from fastapi import APIRouter, HTTPException
from app.models.schemas import TraceRequest
from app.services.engine import trace_code_async
from app.services.jobs import get_job

router = APIRouter(prefix="/v1/trace", tags=["trace"])


@router.post("")
def submit_trace(req: TraceRequest):
    job_id = trace_code_async(req.code)
    return {
        "job_id": job_id,
        "status": "submitted",
    }


@router.get("/{job_id}")
def get_trace(job_id: str):
    job = get_job(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    return job
