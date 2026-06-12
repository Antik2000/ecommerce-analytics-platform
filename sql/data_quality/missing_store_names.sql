SELECT
    COUNT(*) AS missing_store_names
FROM `studied-slate-499209-e8.raw.orders`
WHERE store_name IS NULL;