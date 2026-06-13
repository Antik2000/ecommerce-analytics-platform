import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

PROJECT_ID = "studied-slate-499209-e8"

DATASET = "mart"

TABLE_NAME = "sales_summary"

FULL_TABLE_NAME = (
    f"{PROJECT_ID}.{DATASET}.{TABLE_NAME}"
)