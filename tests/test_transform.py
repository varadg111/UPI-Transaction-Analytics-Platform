import sys
import os
import pandas as pd
import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from transform import transform_data


@pytest.fixture
def sample_df():
    data = {
        "transaction id": ["TXN001", "TXN002", "TXN003"],
        "timestamp": ["2024-01-15 10:30:00", "2024-06-20 22:15:00", "2024-12-05 03:45:00"],
        "transaction type": ["P2P", "P2M", "Bill Payment"],
        "merchant_category": ["Shopping", "Grocery", "Utilities"],
        "amount (INR)": [200, 1500, 8000],
        "transaction_status": ["SUCCESS", "FAILED", "SUCCESS"],
        "fraud_flag": [0, 1, 0],
        "is_weekend": [0, 1, 0],
    }
    return pd.DataFrame(data)


def test_transform_runs_without_error(sample_df):
    result = transform_data(sample_df)
    assert isinstance(result, pd.DataFrame)


def test_row_count_unchanged(sample_df):
    result = transform_data(sample_df)
    assert result.shape[0] == sample_df.shape[0]


def test_transaction_month_format(sample_df):
    result = transform_data(sample_df)
    assert result.loc[0, "transaction_month"] == "2024-01"
    assert result.loc[1, "transaction_month"] == "2024-06"


def test_transaction_quarter(sample_df):
    result = transform_data(sample_df)
    assert result.loc[0, "transaction_quarter"] == "Q1"
    assert result.loc[1, "transaction_quarter"] == "Q2"
    assert result.loc[2, "transaction_quarter"] == "Q4"


def test_amount_bucket_assignment(sample_df):
    result = transform_data(sample_df)
    assert result.loc[0, "amount_bucket"] == "Micro Transaction"    # 200
    assert result.loc[1, "amount_bucket"] == "Medium Transaction"   # 1500
    assert result.loc[2, "amount_bucket"] == "Large Transaction"    # 8000


def test_fraud_status_mapping(sample_df):
    result = transform_data(sample_df)
    assert result.loc[0, "fraud_status"] == "Genuine"
    assert result.loc[1, "fraud_status"] == "Fraud"


def test_transaction_outcome_mapping(sample_df):
    result = transform_data(sample_df)
    assert result.loc[0, "transaction_outcome"] == "Successful"
    assert result.loc[1, "transaction_outcome"] == "Failed"


def test_week_type_mapping(sample_df):
    result = transform_data(sample_df)
    assert result.loc[0, "week_type"] == "Weekday"
    assert result.loc[1, "week_type"] == "Weekend"