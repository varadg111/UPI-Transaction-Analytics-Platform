import logging
logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
import pandas as pd
from extract import extract_data


def transform_data(df):
    """
    Performs all data transformations and feature engineering.
    """

    logging.info("\nStarting Transformation...")

    # Create copy
    df = df.copy()

    # 1. Convert timestamp
    logging.info("Converting timestamp...")
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # 2. Create transaction date
    logging.info("Creating transaction date...")
    df["transaction_date"] = df["timestamp"].dt.date

    # 3. Create transaction month
    logging.info("Creating transaction month...")
    df["transaction_month"] = (
        df["timestamp"]
        .dt.to_period("M")
        .astype(str)
    )

    # 4. Create transaction quarter
    logging.info("Creating transaction quarter...")
    df["transaction_quarter"] = (
        "Q" + df["timestamp"].dt.quarter.astype(str)
    )

    # 5. Create amount bucket
    logging.info("Creating amount buckets...")

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
    logging.info("Creating fraud status...")

    df["fraud_status"] = df["fraud_flag"].map({
        0: "Genuine",
        1: "Fraud"
    })

    # 7. Create transaction outcome
    logging.info("Creating transaction outcome...")

    df["transaction_outcome"] = df["transaction_status"].map({
        "SUCCESS": "Successful",
        "FAILED": "Failed"
    })

    # 8. Create week type
    logging.info("Creating week type...")

    df["week_type"] = df["is_weekend"].map({
        0: "Weekday",
        1: "Weekend"
    })

    logging.info("\nTransformation Completed")
    logging.info(f"Rows: {df.shape[0]}")
    logging.info(f"Columns: {df.shape[1]}")

    return df


if __name__ == "__main__":

    df = extract_data(
        "data\\RAW\\upi_transactions_2024.csv"
    )

    df = transform_data(df)

    logging.info("\nFirst 5 Rows:")
    logging.info(df.head())

    logging.info("\nDataset Shape:")
    logging.info(df.shape)

    logging.info("\nColumns:")
    logging.info(df.columns.tolist())