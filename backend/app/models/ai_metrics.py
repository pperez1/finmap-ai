from sqlalchemy import Column, Integer, Float
from app.core.database import Base

class AIMetric(Base):
    __tablename__ = "ai_metrics"

    id = Column(Integer, primary_key=True)
    accuracy = Column(Float)