SELECT
    COUNT(*) AS negative_revenue_rows
FROM `studied-slate-499209-e8.raw.orders`
WHERE revenue < 0;