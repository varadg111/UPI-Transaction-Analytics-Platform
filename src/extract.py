import logging
logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
import pandas as pd

def extract_data(file_path):
    logging.info("Starting Extraction...")

    df = pd.read_csv(file_path)

    logging.info("Rows Loaded:", df.shape[0])
    logging.info("Columns Loaded:", df.shape[1])

    logging.info("Extraction Completed")

    return df



if __name__ == "__main__":
    df = extract_data(
        r"data\raw\upi_transactions_2024.csv"
    )
    logging.info(df.head())