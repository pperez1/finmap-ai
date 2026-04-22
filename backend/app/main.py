from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes_process import router as process_router

app = FastAPI()

# CORS (safe + simple)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # keep open for now
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(process_router)


@app.get("/health")
def health():
    return {"status": "ok"}