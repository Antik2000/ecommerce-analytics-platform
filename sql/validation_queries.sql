-- =====================================================
-- PIPELINE VALIDATION QUERIES
-- =====================================================

-- Validation 1: Raw Row Count

SELECT
    COUNT(*) AS raw_row_count
FROM `studied-slate-499209-e8.raw.orders`;

-- =====================================================

-- Validation 2: Staging Row Count

SELECT
    COUNT(*) AS staging_row_count
FROM `studied-slate-499209-e8.staging.stg_orders`;

-- =====================================================

-- Validation 3: Mart Row Count

SELECT
    COUNT(*) AS mart_row_count
FROM `studied-slate-499209-e8.mart.sales_summary`;

-- =====================================================

-- Validation 4: Raw Revenue Reconciliation

SELECT
    ROUND(SUM(revenue), 2) AS raw_revenue
FROM `studied-slate-499209-e8.raw.orders`
WHERE revenue >= 0
AND order_date IS NOT NULL;

-- =====================================================

-- Validation 5: Staging Revenue Reconciliation

SELECT
    ROUND(SUM(revenue), 2) AS staging_revenue
FROM `studied-slate-499209-e8.staging.stg_orders`;

-- =====================================================

-- Validation 6: Mart Revenue Reconciliation

SELECT
    ROUND(SUM(total_revenue), 2) AS mart_revenue
FROM `studied-slate-499209-e8.mart.sales_summary`;

-- =====================================================

-- Validation 7: Duplicate Orders In Raw Layer

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

-- =====================================================

-- Validation 8: Negative Revenue Remaining In Staging

SELECT
    COUNT(*) AS negative_revenue_remaining
FROM `studied-slate-499209-e8.staging.stg_orders`
WHERE revenue < 0;

-- =====================================================

-- Validation 9: Missing Order Dates Remaining In Staging

SELECT
    COUNT(*) AS missing_dates_remaining
FROM `studied-slate-499209-e8.staging.stg_orders`
WHERE order_date IS NULL;

-- =====================================================