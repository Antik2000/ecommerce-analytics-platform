from pathlib import Path

from google.cloud import bigquery


PROJECT_ID = "studied-slate-499209-e8"

DQ_FOLDER = "sql/data_quality"


def run_data_quality() -> None:
    """
    Execute all data quality checks.
    """

    dq_path = Path(DQ_FOLDER)

    if not dq_path.exists():
        raise FileNotFoundError(
            f"Folder not found: {DQ_FOLDER}"
        )

    client = bigquery.Client(
        project=PROJECT_ID
    )

    print("\n" + "=" * 50)
    print("DATA QUALITY REPORT")
    print("=" * 50)

    sql_files = sorted(
        dq_path.glob("*.sql")
    )

    for sql_file in sql_files:

        sql_query = sql_file.read_text(
            encoding="utf-8"
        )

        query_job = client.query(
            sql_query
        )

        results = list(
            query_job.result()
        )

        if results:

            row = dict(results[0].items())

            metric_name = list(
                row.keys()
            )[0]

            metric_value = list(
                row.values()
            )[0]

            print(
                f"{metric_name:<30}: {metric_value}"
            )

    print("=" * 50)
    print("DATA QUALITY CHECK COMPLETE")
    print("=" * 50)


if __name__ == "__main__":
    run_data_quality()