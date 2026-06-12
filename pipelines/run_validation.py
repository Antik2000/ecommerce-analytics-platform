from google.cloud import bigquery


PROJECT_ID = "studied-slate-499209-e8"


def run_validation() -> None:
    """
    Execute pipeline validation checks.
    """

    client = bigquery.Client(
        project=PROJECT_ID
    )

    print("\n" + "=" * 50)
    print("PIPELINE VALIDATION REPORT")
    print("=" * 50)

    validation_queries = [

        (
            "raw_row_count",
            """
            SELECT COUNT(*) AS value
            FROM `studied-slate-499209-e8.raw.orders`
            """
        ),

        (
            "staging_row_count",
            """
            SELECT COUNT(*) AS value
            FROM `studied-slate-499209-e8.staging.stg_orders`
            """
        ),

        (
            "mart_row_count",
            """
            SELECT COUNT(*) AS value
            FROM `studied-slate-499209-e8.mart.sales_summary`
            """
        ),

        (
            "raw_valid_revenue",
            """
            SELECT ROUND(SUM(revenue),2) AS value
            FROM `studied-slate-499209-e8.raw.orders`
            WHERE revenue >= 0
            AND order_date IS NOT NULL
            """
        ),

        (
            "staging_revenue",
            """
            SELECT ROUND(SUM(revenue),2) AS value
            FROM `studied-slate-499209-e8.staging.stg_orders`
            """
        ),

        (
            "mart_revenue",
            """
            SELECT ROUND(SUM(total_revenue),2) AS value
            FROM `studied-slate-499209-e8.mart.sales_summary`
            """
        ),

        (
            "duplicate_orders",
            """
            SELECT COUNT(*) AS value
            FROM (
                SELECT
                    order_id
                FROM `studied-slate-499209-e8.raw.orders`
                GROUP BY order_id
                HAVING COUNT(*) > 1
            )
            """
        ),

        (
            "negative_revenue_remaining",
            """
            SELECT COUNT(*) AS value
            FROM `studied-slate-499209-e8.staging.stg_orders`
            WHERE revenue < 0
            """
        ),

        (
            "missing_dates_remaining",
            """
            SELECT COUNT(*) AS value
            FROM `studied-slate-499209-e8.staging.stg_orders`
            WHERE order_date IS NULL
            """
        )

    ]

    for metric_name, sql_query in validation_queries:

        query_job = client.query(
            sql_query
        )

        results = list(
            query_job.result()
        )

        metric_value = results[0]["value"]

        print(
            f"{metric_name:<30}: {metric_value}"
        )

    print("=" * 50)
    print("VALIDATION COMPLETE")
    print("=" * 50)


if __name__ == "__main__":
    run_validation()