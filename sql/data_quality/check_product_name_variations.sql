SELECT
    COUNT(*) AS product_variations
FROM (
    SELECT
        UPPER(TRIM(product_name)) AS standardized_product
    FROM `studied-slate-499209-e8.raw.orders`
    GROUP BY standardized_product
    HAVING COUNT(DISTINCT product_name) > 1
);