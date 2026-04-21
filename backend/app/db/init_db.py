from sqlalchemy import text
from app.db import engine

def init_db():
    with engine.begin() as conn:
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS uploads (
            id SERIAL PRIMARY KEY,
            filename TEXT,
            mapping JSONB,
            missing_fields JSONB,
            unmapped_columns JSONB,
            created_at TIMESTAMP DEFAULT NOW()
        );
        """))