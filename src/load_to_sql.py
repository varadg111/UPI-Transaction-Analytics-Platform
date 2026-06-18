import urllib

from sqlalchemy import create_engine

from extract import extract_data
from transform import transform_data

# Extract
df = extract_data(
    r"data\Raw\upi_transactions_2024.csv"
)

# Transform
df = transform_data(df)

# Rename columns to match SQL table
df = df.rename(columns={
    "transaction id": "transaction_id",
    "transaction type": "transaction_type",
    "amount (INR)": "amount_inr"
})

print(df.columns.tolist())

# SQL Connection
params = urllib.parse.quote_plus(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=UPI_Analytics;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

engine = create_engine(
    f"mssql+pyodbc:///?odbc_connect={params}"
)

print("Loading data into SQL Server...")

# Load into SQL Server
df.to_sql(
    name="Fact_Transactions",
    con=engine,
    if_exists="append",
    index=False,
    chunksize=5000
)

print("Data Loaded Successfully")