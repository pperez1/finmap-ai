from fastapi import APIRouter, UploadFile
import pandas as pd

router = APIRouter()

@router.post("/upload")
async def upload(file: UploadFile):
    df = pd.read_excel(file.file)
    return {"columns": df.columns.tolist()}