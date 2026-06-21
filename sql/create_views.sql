-- =========================================================
-- UPI Transaction Analytics Platform
-- Analytical Views for Power BI Dashboard
-- =========================================================

-- 1. Daily transaction summary
CREATE OR ALTER VIEW vw_daily_transaction_summary AS
SELECT
    transaction_date,
    COUNT(*) AS total_transactions,
    SUM(amount_inr) AS total_amount,
    SUM(CASE WHEN transaction_status = 'SUCCESS' THEN 1 ELSE 0 END) AS successful_transactions,
    SUM(CASE WHEN transaction_status = 'FAILED' THEN 1 ELSE 0 END) AS failed_transactions
FROM Fact_Transactions
GROUP BY transaction_date;
GO

-- 2. Bank performance: volume and value per bank
CREATE OR ALTER VIEW vw_bank_performance AS
SELECT
    sender_bank,
    COUNT(*) AS transaction_count,
    SUM(amount_inr) AS transaction_value
FROM Fact_Transactions
GROUP BY sender_bank;
GO

-- 3. Fraud analysis by state
CREATE OR ALTER VIEW vw_fraud_analysis AS
SELECT
    sender_state,
    COUNT(*) AS total_transactions,
    SUM(CAST(fraud_flag AS INT)) AS fraud_transactions,
    ROUND(
        100.0 * SUM(CAST(fraud_flag AS INT)) / COUNT(*),
        2
    ) AS fraud_rate_pct
FROM Fact_Transactions
GROUP BY sender_state;
GO

-- 4. Daily success/failure rate
-- (fixed: original had "---COUNT(*)" which commented out the whole line)
CREATE OR ALTER VIEW vw_transaction_success_summary AS
SELECT
    transaction_date,
    COUNT(*) AS total_transactions,
    SUM(CASE WHEN transaction_status = 'SUCCESS' THEN 1 ELSE 0 END) AS successful_transactions,
    SUM(CASE WHEN transaction_status = 'FAILED' THEN 1 ELSE 0 END) AS failed_transactions,
    ROUND(
        100.0 *
        SUM(CASE WHEN transaction_status = 'SUCCESS' THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS success_rate
FROM Fact_Transactions
GROUP BY transaction_date;
GO

-- 5. Monthly performance trend
CREATE OR ALTER VIEW vw_monthly_performance AS
SELECT
    transaction_month,
    COUNT(*) AS transaction_count,
    SUM(amount_inr) AS transaction_value,
    AVG(amount_inr) AS average_transaction_value
FROM Fact_Transactions
GROUP BY transaction_month;
GO

-- 6. Fraud by device type (supports Fraud Analytics dashboard page)
CREATE OR ALTER VIEW vw_fraud_by_device AS
SELECT
    device_type,
    COUNT(*) AS total_transactions,
    SUM(CAST(fraud_flag AS INT)) AS fraud_transactions,
    ROUND(
        100.0 * SUM(CAST(fraud_flag AS INT)) / COUNT(*),
        2
    ) AS fraud_rate_pct
FROM Fact_Transactions
GROUP BY device_type;
GO

-- 7. Fraud by network type (supports Fraud Analytics dashboard page)
CREATE OR ALTER VIEW vw_fraud_by_network AS
SELECT
    network_type,
    COUNT(*) AS total_transactions,
    SUM(CAST(fraud_flag AS INT)) AS fraud_transactions,
    ROUND(
        100.0 * SUM(CAST(fraud_flag AS INT)) / COUNT(*),
        2
    ) AS fraud_rate_pct
FROM Fact_Transactions
GROUP BY network_type;
GO
