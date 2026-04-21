import os
from dotenv import load_dotenv

ENV = os.getenv("ENV", "dev")
load_dotenv(f".env.{ENV}")

AI_CANARY_PERCENT = int(os.getenv("AI_CANARY_PERCENT", 0))