# UPI Transaction Analytics Platform

End-to-end analytics platform for monitoring UPI digital payment transactions — built with Python, SQL Server, and Power BI to track transaction performance, detect fraud patterns, and surface bank and merchant insights.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![SQL Server](https://img.shields.io/badge/database-SQL%20Server-red.svg)
![Power BI](https://img.shields.io/badge/visualization-Power%20BI-yellow.svg)

---

## Problem

Digital payment providers process millions of UPI transactions daily. Manually tracking success rates, fraud incidents, merchant performance, and bank-level trends across this volume is impractical. This project builds an automated pipeline that ingests raw transaction data, structures it for analysis, and surfaces the metrics that matter — without manual spreadsheet work.

---

## Architecture

![Architecture](docs/architecture.png)

```
UPI Transactions Dataset (CSV)
            │
            ▼
   Extract Layer (extract.py)
            │
            ▼
  Transform Layer (transform.py)
   - Feature engineering
   - Data quality checks
            │
            ▼
   Load Layer (load.py / load_to_sql.py)
            │
            ▼
      SQL Server Database
      (Fact_Transactions)
            │
            ▼
        SQL Views
   (aggregated for reporting)
            │
            ▼
     Power BI Dashboards
```

---

## Dashboard Screenshots

### Executive Overview
High-level view of transaction volume, transaction value, success rate, and fraud count.

![Executive Overview](docs/dashboard_screenshots/executive_overview.png)

### Fraud Analytics
Fraud incidents broken down by state, device type, and network type.

![Fraud Analytics](docs/dashboard_screenshots/fraud_analytics.png)

### Bank Performance
Transaction volume, transaction value, and market share by bank.

![Bank Performance](docs/dashboard_screenshots/bank_performance.png)

### Executive Dashboard
Interactive filters across month, state, transaction type, and merchant category.

![Executive Dashboard](docs/dashboard_screenshots/executive_dashboard.png)

---

## Tech Stack

| Layer | Tools |
|---|---|
| Language | Python |
| Data Processing | Pandas, NumPy |
| Database | SQL Server, SQLAlchemy, PyODBC |
| Visualization | Power BI |
| Version Control | Git, GitHub |

---

## Dataset

| Attribute | Details |
|---|---|
| Source | Kaggle — UPI Transactions 2024 |
| Records | 250,000+ |
| Columns | 24 |
| Domain | FinTech / Digital Payments |
| Format | CSV |

Key fields: transaction ID, timestamp, transaction type, merchant category, amount, status, sender/receiver bank, sender state, device type, network type, fraud flag.

---

## How to Run

```bash
# 1. Clone the repo
git clone https://github.com/varadg111/UPI-Transaction-Analytics-Platform.git
cd UPI-Transaction-Analytics-Platform

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure your database connection
# Update the connection string in src/load_to_sql.py with your own
# SQL Server instance details

# 4. Run the ETL pipeline
python src/main.py

# 5. Create SQL views (run once against your database)
# Execute sql/create_tables.sql and sql/create_views.sql in
# SQL Server Management Studio

# 6. Open the dashboard
# Open dashboard/UPI_Analytics.pbix in Power BI Desktop and
# refresh the data source
```

---

## ETL Pipeline

**Extract** (`src/extract.py`)
Reads the raw transaction CSV and validates basic schema before passing it downstream.

**Transform** (`src/transform.py`)
Engineers business-ready features:
- `transaction_date`, `transaction_month`, `transaction_quarter`
- `amount_bucket` — categorized transaction size
- `fraud_status`, `transaction_outcome`
- `week_type` — weekday vs weekend

**Load** (`src/load.py`, `src/load_to_sql.py`)
Loads the transformed dataset into SQL Server in chunked batches, ready for SQL-based reporting.

---

## SQL Layer

The processed data is loaded into a single `Fact_Transactions` table in SQL Server, with the following analytical views built on top:

| View | Purpose |
|---|---|
| `vw_daily_transaction_summary` | Daily transaction volume, value, and success/failure counts |
| `vw_bank_performance` | Transaction count and value by bank |
| `vw_fraud_analysis` | Fraud count and rate by state |
| `vw_fraud_by_device` | Fraud count and rate by device type |
| `vw_fraud_by_network` | Fraud count and rate by network type |
| `vw_transaction_success_summary` | Daily success rate calculation |
| `vw_monthly_performance` | Monthly transaction count, value, and average ticket size |

> **Design note:** this project uses a single denormalized fact table rather than a fully normalized star schema. This was a deliberate simplicity trade-off for a dataset of this size — the views above provide the same reporting flexibility without the join overhead of separate dimension tables.

---

## Power BI Dashboards

- **Executive Overview** — Total transactions, transaction value, success rate, fraud count, monthly trend
- **Fraud Analytics** — Fraud by state, device type, network type
- **Bank Performance** — Bank market share, transaction volume and value by bank
- **Executive Dashboard** — Interactive filters, merchant category breakdown, state-level analysis

---

## Key Insights

- Overall transaction success rate is above 95%, indicating strong platform reliability.
- Fraud transactions represent a small fraction of total volume, but are concentrated more heavily on Android devices and certain network types — suggesting fraud monitoring should be weighted by channel, not applied uniformly.
- Shopping and Grocery merchant categories drive the highest transaction value, while Utilities and Fuel contribute more to transaction *volume* than value — a useful distinction for merchant partnership prioritization.
- A small number of banks account for a disproportionate share of transaction volume, which has implications for partnership negotiation leverage and infrastructure load planning.

---

## Limitations & Future Work

This project currently focuses on descriptive analytics (what happened) rather than predictive analytics (what's likely to happen next). Planned next steps:

- **Fraud prediction model** — train a classifier (logistic regression / XGBoost) on the engineered features, evaluated on precision/recall rather than accuracy given class imbalance, with risk scores surfaced back into the dashboard.
- **Automated testing** — unit tests on transform logic, run via GitHub Actions on each push.
- **Data validation layer** — explicit null/duplicate/schema checks with logging, rather than relying on clean input data.
- **Cloud deployment** — migrate the pipeline to Azure Data Factory / Microsoft Fabric for scheduled, production-style ingestion.

---

## Author

**Varad Gandhi**
Final-Year Dual Degree Student

- B.E. Electronics & Computer Science
- B.Sc. Data Science (IIT Madras)

### Connect

- LinkedIn: https://www.linkedin.com/in/varad-gandhi-15a9b9291/
- Email: gandhivarad1@gmail.com

### Skills

Python • SQL • Power BI • Excel • SQL Server • Azure • Microsoft Fabric • ETL Pipelines • Data Analytics

---

## License

This project is licensed under the MIT License — see LICENSE file for details.

---

Quick reminder before you push: make sure `docs/architecture.png` matches your actual saved filename exactly (case-sensitive), and that `requirements.txt` and a real `LICENSE` file exist in your repo root — otherwise those links/instructions will break. Want me to generate those two files now?
