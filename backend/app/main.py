from fastapi import FastAPI

from app.api.routes_flags import router as flags_router
from app.api.routes_billing import router as billing_router
from app.api.routes_ai_eval import router as ai_router
from app.api.routes_compliance_export import router as compliance_router
from app.api.routes_mapping import router as mapping_router
from app.api.routes_upload import router as upload_router
from app.api.routes_process import router as process_router
from app.models.mapping import Base
from app.models.db import engine

app = FastAPI()

app.include_router(flags_router)
app.include_router(billing_router)
app.include_router(ai_router)
app.include_router(compliance_router)
app.include_router(mapping_router)
app.include_router(upload_router)
app.include_router(process_router)

Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    return {"status": "ok"}

