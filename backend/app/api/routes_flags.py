from fastapi import APIRouter

router = APIRouter()

@router.get("/flags")
def flags():
    return [{"name": "ai_canary", "enabled": True}]