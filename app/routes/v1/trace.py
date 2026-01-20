from fastapi import APIRouter, HTTPException, Request
from app.models.schemas import TraceRequest
from app.services.engine import trace_code_async
from app.services.jobs import get_job
from app.guards.rate_limit import rate_limit

router = APIRouter(prefix="/v1/trace", tags=["trace"])


@router.post("")
def submit_trace(req: TraceRequest, request: Request):
    rate_limit(request)

    job_id = trace_code_async(req.code)
    return {
        "job_id": job_id,
        "status": "submitted",
        "request_id": request.state.request_id,
        "trace_id": request.state.trace_id,
    }


@router.get("/{job_id}")
def get_trace(job_id: str, request: Request):
    job = get_job(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    return {
        **job,
        "request_id": request.state.request_id,
        "trace_id": request.state.trace_id,
    }
