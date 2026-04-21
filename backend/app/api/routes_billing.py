from fastapi import APIRouter

router = APIRouter()

@router.get("/billing")
def billing():
    return {"monthly_cost": 1200}