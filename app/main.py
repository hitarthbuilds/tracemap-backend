from fastapi import FastAPI

from app.routes.trace import router as trace_router

app = FastAPI(title="TraceMap Backend")

app.include_router(trace_router)
