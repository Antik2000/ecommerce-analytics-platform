SELECT
    COUNT(*) AS duplicate_orders
FROM (
    SELECT
        order_id,
        COUNT(*) AS cnt
    FROM `studied-slate-499209-e8.raw.orders`
    GROUP BY order_id
    HAVING COUNT(*) > 1
);