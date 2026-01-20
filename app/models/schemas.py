from pydantic import BaseModel, Field


class TraceRequest(BaseModel):
    """
    Request payload for tracing Python code.
    """
    code: str = Field(..., description="Python source code to execute and trace")


class TraceResponse(BaseModel):
    """
    Response payload containing execution snapshot.
    """
    snapshot: dict
    node_count: int
