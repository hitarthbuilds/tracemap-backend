from fastapi import APIRouter

router = APIRouter(prefix="/v1/health", tags=["health"])


@router.get("")
def health():
    return {
        "status": "ok",
        "engine": "tracemap",
        "version": "0.1.0",
    }
