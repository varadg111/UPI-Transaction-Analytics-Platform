-- =========================================================
-- UPI Transaction Analytics Platform
-- Database & Table Creation Script
-- =========================================================

-- Uncomment these two lines if running for the first time
-- CREATE DATABASE UPI_Analytics;
-- GO
-- USE UPI_Analytics;
-- GO

-- Drop table if it already exists (useful when re-running this script during development)
IF OBJECT_ID('Fact_Transactions', 'U') IS NOT NULL
    DROP TABLE Fact_Transactions;
GO

CREATE TABLE Fact_Transactions (

    transaction_id        VARCHAR(20)     NOT NULL PRIMARY KEY,

    transaction_timestamp DATETIME        NOT NULL,

    transaction_type      VARCHAR(50)     NOT NULL,

    merchant_category     VARCHAR(50)     NULL,

    amount_inr            DECIMAL(12,2)   NOT NULL,

    transaction_status    VARCHAR(20)     NOT NULL,

    sender_age_group      VARCHAR(20)     NULL,

    receiver_age_group    VARCHAR(20)     NULL,

    sender_state          VARCHAR(50)     NULL,

    sender_bank           VARCHAR(50)     NULL,

    receiver_bank         VARCHAR(50)     NULL,

    device_type           VARCHAR(20)     NULL,

    network_type          VARCHAR(20)     NULL,

    fraud_flag             BIT             NOT NULL DEFAULT 0,

    hour_of_day            INT             NULL,

    day_of_week            VARCHAR(20)     NULL,

    is_weekend              BIT             NOT NULL DEFAULT 0,

    transaction_date        DATE            NOT NULL,

    transaction_month       VARCHAR(10)     NULL,

    transaction_quarter     VARCHAR(5)      NULL,

    amount_bucket           VARCHAR(30)     NULL,

    fraud_status             VARCHAR(20)     NULL,

    transaction_outcome      VARCHAR(20)     NULL,

    week_type                VARCHAR(20)     NULL,

    -- Basic data quality constraints
    CONSTRAINT CHK_amount_positive CHECK (amount_inr >= 0),
    CONSTRAINT CHK_transaction_status CHECK (transaction_status IN ('SUCCESS', 'FAILED', 'PENDING'))
);
GO

-- Helpful indexes for the columns the dashboard filters/groups by most
CREATE INDEX IX_Fact_Transactions_Date ON Fact_Transactions(transaction_date);
CREATE INDEX IX_Fact_Transactions_State ON Fact_Transactions(sender_state);
CREATE INDEX IX_Fact_Transactions_Bank ON Fact_Transactions(sender_bank);
CREATE INDEX IX_Fact_Transactions_Fraud ON Fact_Transactions(fraud_flag);
GO
