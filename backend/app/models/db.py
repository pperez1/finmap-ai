import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL")

engine = None

def get_engine():
    global engine
    if engine:
        return engine

    for i in range(10):
        try:
            engine = create_engine(DATABASE_URL)
            conn = engine.connect()
            conn.close()
            print("✅ Connected to DB")
            return engine
        except Exception as e:
            print(f"⏳ DB not ready, retrying... ({i+1}/10)")
            time.sleep(2)

    raise Exception("❌ Could not connect to DB after retries")

engine = get_engine()
SessionLocal = sessionmaker(bind=engine)