from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("")
async def health():
    return {
        "status": "ok",
        "service": "MatchAI API",
        "version": "0.1.0",
    }