from extract import extract_data
from transform import transform_data
from load import load_data

if __name__ == "__main__":
    raw_path = "data/raw/upi_transactions_2024.csv"
    processed_path = "data/processed/upi_transactions_processed.csv"

    print("=== Starting Full ETL Pipeline ===")

    df = extract_data(raw_path)
    df = transform_data(df)
    load_data(df, processed_path)

    print("=== Pipeline Completed Successfully ===")