import pandas as pd
from extract import extract_data


def transform_data(df):
    """
    Performs all data transformations and feature engineering.
    """

    print("\nStarting Transformation...")

    # Create copy
    df = df.copy()

    # 1. Convert timestamp
    print("Converting timestamp...")
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # 2. Create transaction date
    print("Creating transaction date...")
    df["transaction_date"] = df["timestamp"].dt.date

    # 3. Create transaction month
    print("Creating transaction month...")
    df["transaction_month"] = (
        df["timestamp"]
        .dt.to_period("M")
        .astype(str)
    )

    # 4. Create transaction quarter
    print("Creating transaction quarter...")
    df["transaction_quarter"] = (
        "Q" + df["timestamp"].dt.quarter.astype(str)
    )

    # 5. Create amount bucket
    print("Creating amount buckets...")

    bins = [0, 500, 1000, 5000, 10000, float("inf")]

    labels = [
        "Micro Transaction",
        "Small Transaction",
        "Medium Transaction",
        "Large Transaction",
        "Premium Transaction"
    ]

    df["amount_bucket"] = pd.cut(
        df["amount (INR)"],
        bins=bins,
        labels=labels
    )

    # 6. Create fraud status
    print("Creating fraud status...")

    df["fraud_status"] = df["fraud_flag"].map({
        0: "Genuine",
        1: "Fraud"
    })

    # 7. Create transaction outcome
    print("Creating transaction outcome...")

    df["transaction_outcome"] = df["transaction_status"].map({
        "SUCCESS": "Successful",
        "FAILED": "Failed"
    })

    # 8. Create week type
    print("Creating week type...")

    df["week_type"] = df["is_weekend"].map({
        0: "Weekday",
        1: "Weekend"
    })

    print("\nTransformation Completed")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    return df


if __name__ == "__main__":

    df = extract_data(
        "data\\RAW\\upi_transactions_2024.csv"
    )

    df = transform_data(df)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nDataset Shape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())