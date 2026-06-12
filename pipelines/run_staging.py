from pathlib import Path

from google.cloud import bigquery


PROJECT_ID = "studied-slate-499209-e8"

SQL_FILE = "sql/stg_orders.sql"


def run_staging() -> None:
    """
    Execute staging transformation.
    """

    sql_path = Path(SQL_FILE)

    if not sql_path.exists():
        raise FileNotFoundError(
            f"SQL file not found: {SQL_FILE}"
        )

    print(f"Reading SQL from: {SQL_FILE}")

    sql_query = sql_path.read_text(
        encoding="utf-8"
    )

    client = bigquery.Client(
        project=PROJECT_ID
    )

    print("Executing staging transformation...")

    job = client.query(sql_query)

    job.result()

    table_ref = (
        f"{PROJECT_ID}.staging.stg_orders"
    )

    table = client.get_table(
        table_ref
    )

    print(
        f"Rows in staging table: {table.num_rows}"
    )

    print(
        "Successfully created staging.stg_orders"
    )


if __name__ == "__main__":
    run_staging()