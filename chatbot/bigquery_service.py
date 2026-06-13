from google.cloud import bigquery
from google.oauth2 import service_account
import streamlit as st
import pandas as pd

from config import PROJECT_ID

credentials = service_account.Credentials.from_service_account_info(
    dict(st.secrets["gcp_service_account"])
)

client = bigquery.Client(
    credentials=credentials,
    project=PROJECT_ID
)

def execute_query(sql: str) -> pd.DataFrame:

    cleaned_sql = sql.strip().upper()

    if not (
        cleaned_sql.startswith("SELECT")
        or cleaned_sql.startswith("WITH")
    ):
        raise ValueError(
            "Only SELECT queries are allowed."
        )

    query_job = client.query(sql)

    results = query_job.result()

    return results.to_dataframe()