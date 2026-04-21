from fastapi import APIRouter, UploadFile
import pandas as pd
from app.services.mapping_service import hybrid_map

router = APIRouter()

@router.post("/process")
async def process(file: UploadFile):
    df = pd.read_excel(file.file)

    columns = df.columns.tolist()
    mapping = hybrid_map(columns)

    required = ["Revenue", "OperatingCost", "DSCR"]

    missing = [f for f in required if f not in mapping]

    unmapped = [c for c in columns if c not in mapping.values()]

    return {
        "columns": columns,
        "mapping": mapping,
        "missing_fields": missing,
        "unmapped_columns": unmapped
    }