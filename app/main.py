from fastapi import FastAPI
from app.routes.v1.trace import router as trace_v1_router
from app.routes.v1.health import router as health_v1_router

app = FastAPI(title="TraceMap Backend", version="0.1.0")

app.include_router(trace_v1_router)
app.include_router(health_v1_router)
