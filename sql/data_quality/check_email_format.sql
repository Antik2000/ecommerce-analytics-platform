SELECT
    COUNT(*) AS invalid_emails
FROM `studied-slate-499209-e8.raw.orders`
WHERE NOT REGEXP_CONTAINS(
    customer_email,
    r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
);