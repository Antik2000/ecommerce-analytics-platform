CREATE OR REPLACE TABLE
  `studied-slate-499209-e8.staging.stg_orders`
AS

SELECT
    order_id,

    customer_id,

    customer_name,

    customer_email,

    order_date,

    shipping_city,

    shipping_state,

    shipping_country,

    shipping_cost,

    product_id,

    TRIM(UPPER(product_name)) AS product_name,

    category,

    quantity,

    unit_price,

    revenue,

    COALESCE(store_name, 'Unknown Store') AS store_name,

    payment_method,

    order_status

FROM
(
    SELECT
        *,
        ROW_NUMBER() OVER(
            PARTITION BY order_id
            ORDER BY order_date DESC
        ) AS rn

    FROM `studied-slate-499209-e8.raw.orders`
)

WHERE rn = 1
AND revenue >= 0
AND order_date IS NOT NULL;