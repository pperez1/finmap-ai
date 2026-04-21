import random
from app.models.feature_flag import FeatureFlag
from app.core.database import SessionLocal

def is_enabled(flag_name):
    db = SessionLocal()
    flag = db.query(FeatureFlag).filter_by(name=flag_name).first()

    if not flag or not flag.enabled:
        return False

    return random.randint(1, 100) <= flag.rollout_percentage