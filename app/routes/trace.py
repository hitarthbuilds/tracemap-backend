from fastapi import APIRouter, HTTPException

from app.models.schemas import TraceRequest, TraceResponse
from app.services.engine import trace_code
from app.guards.limits import ExecutionTimeout

router = APIRouter()


@router.post("/trace", response_model=TraceResponse)
def trace_endpoint(req: TraceRequest):
    try:
        snapshot = trace_code(req.code)
        return {
            "snapshot": snapshot,
            "node_count": snapshot.get("node_count", 0),
        }
    except ExecutionTimeout as e:
        raise HTTPException(status_code=408, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
