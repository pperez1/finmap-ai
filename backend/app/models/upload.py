from sqlalchemy import Column, Integer, String, JSON, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class Upload(Base):
    __tablename__ = "uploads"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    mapping = Column(JSON)
    missing_fields = Column(JSON)
    unmapped_columns = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)