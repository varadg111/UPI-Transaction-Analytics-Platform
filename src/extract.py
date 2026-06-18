import pandas as pd

def extract_data(file_path):
    print("Starting Extraction...")

    df = pd.read_csv(file_path)

    print("Rows Loaded:", df.shape[0])
    print("Columns Loaded:", df.shape[1])

    print("Extraction Completed")

    return df



df = extract_data(
    r"C:\Users\varad\Downloads\Automated-Transaction-ETL-Pipeline\data\raw\upi_transactions_2024.csv"
)

print(df.head())