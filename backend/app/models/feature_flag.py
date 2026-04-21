from sqlalchemy import Column, Integer, String, Boolean
from app.core.database import Base

class FeatureFlag(Base):
    __tablename__ = "feature_flags"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    enabled = Column(Boolean)
    rollout_percentage = Column(Integer)