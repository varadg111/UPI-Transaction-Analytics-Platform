import logging
logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
from extract import extract_data
from transform import transform_data


def load_data(df, output_path):
    """
    Save transformed dataframe to CSV
    """

    logging.info("Starting Load Process...")

    df.to_csv(output_path, index=False)

    logging.info("File Saved Successfully")
    logging.info(f"Rows Saved: {df.shape[0]}")
    logging.info(f"Columns Saved: {df.shape[1]}")
    logging.info(f"Output File: {output_path}")

    logging.info("Load Completed")


if __name__ == "__main__":

    # Extract
    df = extract_data(
        r"data\Raw\upi_transactions_2024.csv"
    )

    # Transform
    df = transform_data(df)

    # Load
    load_data(
        df,
        r"data\processed\upi_transactions_processed.csv"
    )