import random
from app.core.config import AI_CANARY_PERCENT

def route(prompt):

    if random.randint(1, 100) <= AI_CANARY_PERCENT:
        return f"CANARY: {prompt}"

    return f"STABLE: {prompt}"