CREATE OR REPLACE TABLE
  `studied-slate-499209-e8.mart.sales_summary`
AS

SELECT

    DATE_TRUNC(
        DATE(order_date),
        MONTH
    ) AS sales_month,

    store_name,

    category,

    COUNT(DISTINCT order_id) AS total_orders,

    COUNT(DISTINCT customer_id) AS unique_customers,

    SUM(quantity) AS total_quantity,

    ROUND(SUM(revenue), 2) AS total_revenue,

    ROUND(AVG(revenue), 2) AS avg_order_value,

    CURRENT_TIMESTAMP() AS created_at

FROM
    `studied-slate-499209-e8.staging.stg_orders`

GROUP BY
    sales_month,
    store_name,
    category;