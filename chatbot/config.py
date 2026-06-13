import os
from dotenv import load_dotenv

try:
    import streamlit as st
except ImportError:
    st = None

load_dotenv()

if st and hasattr(st, "secrets"):
    OPENAI_API_KEY = st.secrets.get(
        "OPENAI_API_KEY",
        os.getenv("OPENAI_API_KEY")
    )
else:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

PROJECT_ID = "studied-slate-499209-e8"

DATASET = "mart"

TABLE_NAME = "sales_summary"

FULL_TABLE_NAME = (
    f"{PROJECT_ID}.{DATASET}.{TABLE_NAME}"
)