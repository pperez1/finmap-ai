from fastapi import APIRouter

router = APIRouter()

@router.get("/ai/metrics")
def metrics():
    return {"accuracy": 0.92}