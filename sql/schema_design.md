# Database Schema Design

## Fact_Transactions

| Column             |
| ------------------ |
| transaction_id     |
| amount_inr         |
| transaction_type   |
| transaction_status |
| sender_bank        |
| receiver_bank      |
| fraud_flag         |

## Dim_Date

| Column              |
| ------------------- |
| transaction_date    |
| transaction_month   |
| transaction_quarter |
| day_of_week         |
| week_type           |

## Dim_Customer

| Column             |
| ------------------ |
| sender_age_group   |
| receiver_age_group |
| sender_state       |

## Dim_Device

| Column       |
| ------------ |
| device_type  |
| network_type |

## Dim_Merchant

| Column            |
| ----------------- |
| merchant_category |
