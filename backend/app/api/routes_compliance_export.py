from fastapi import APIRouter
from app.compliance.audit_bundle import build_bundle

router = APIRouter()

@router.get("/compliance/export")
def export():
    return build_bundle()