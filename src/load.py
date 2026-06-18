from extract import extract_data
from transform import transform_data


def load_data(df, output_path):
    """
    Save transformed dataframe to CSV
    """

    print("\nStarting Load Process...")

    df.to_csv(output_path, index=False)

    print("File Saved Successfully")
    print(f"Rows Saved: {df.shape[0]}")
    print(f"Columns Saved: {df.shape[1]}")
    print(f"Output File: {output_path}")

    print("Load Completed")


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