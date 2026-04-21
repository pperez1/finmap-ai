from fastapi import APIRouter
from app.services.mapping_service import hybrid_map

router = APIRouter()

@router.post("/map")
def map_columns(columns: list[str]):
    return hybrid_map(columns)