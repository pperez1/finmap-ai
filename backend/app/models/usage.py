from sqlalchemy import Column, Integer, Float
from app.core.database import Base

class UsageEvent(Base):
    __tablename__ = "usage"

    id = Column(Integer, primary_key=True)
    cost = Column(Float)