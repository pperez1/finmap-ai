from fastapi import APIRouter, UploadFile, File
import pandas as pd
from app.services.mapping_service import hybrid_map
import traceback

router = APIRouter()


@router.post("/process")
async def process(file: UploadFile = File(...)):
    try:
        df = pd.read_excel(file.file)
        columns = df.columns.tolist()

        result = hybrid_map(columns)

        return {
            "status": "success",
            "columns": columns,
            **result
        }

    except Exception as e:
        print("PROCESS ERROR:", str(e))
        print(traceback.format_exc())

        return {
            "status": "error",
            "message": str(e),
            "columns": [],
            "mapping": {},
            "missing_fields": [],
            "unmapped_columns": []
        }