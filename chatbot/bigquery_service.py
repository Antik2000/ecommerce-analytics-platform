from google.cloud import bigquery
import pandas as pd

from config import PROJECT_ID

client = bigquery.Client(
    project=PROJECT_ID
)

def execute_query(sql: str) -> pd.DataFrame:
    """
    Execute BigQuery SQL and return results as DataFrame.
    """

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