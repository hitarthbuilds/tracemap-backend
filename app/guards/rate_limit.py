import time
from fastapi import Request, HTTPException

# 10 requests per 60 seconds
WINDOW = 60
MAX_REQUESTS = 10

REQUESTS = {}


def rate_limit(request: Request):
    ip = request.client.host
    now = time.time()

    timestamps = REQUESTS.get(ip, [])
    timestamps = [t for t in timestamps if now - t < WINDOW]

    if len(timestamps) >= MAX_REQUESTS:
        raise HTTPException(
            status_code=429,
            detail="Too many requests. Slow down."
        )

    timestamps.append(now)
    REQUESTS[ip] = timestamps
