from pathlib import Path
import pandas as pd
from google.cloud import bigquery


PROJECT_ID = "studied-slate-499209-e8"
DATASET_ID = "raw"
TABLE_ID = "orders"


def load_raw(csv_file_path: str) -> None:
    """
    Load source CSV into BigQuery raw.orders table.
    """

    csv_path = Path(csv_file_path)

    if not csv_path.exists():
        raise FileNotFoundError(
            f"File not found: {csv_file_path}"
        )

    print(f"Reading file: {csv_file_path}")

    df = pd.read_csv(csv_path)

    print(f"Rows found in source file: {len(df)}")

    client = bigquery.Client(
        project=PROJECT_ID
    )

    table_ref = (
        f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"
    )

    job_config = bigquery.LoadJobConfig(
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
    )

    print(f"Loading data into {table_ref}...")

    job = client.load_table_from_dataframe(
        df,
        table_ref,
        job_config=job_config
    )

    job.result()

    table = client.get_table(table_ref)

    print(
        f"Rows in BigQuery table: {table.num_rows}"
    )

    print(
        f"Successfully loaded data into {table_ref}"
    )


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        raise ValueError(
            "Usage: python load_raw.py <csv_file_path>"
        )

    load_raw(sys.argv[1])