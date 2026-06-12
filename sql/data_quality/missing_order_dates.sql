SELECT
    COUNT(*) AS missing_order_dates
FROM `studied-slate-499209-e8.raw.orders`
WHERE order_date IS NULL;