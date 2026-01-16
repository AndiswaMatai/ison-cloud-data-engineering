import pandas as pd

def test_no_negative_amounts():
    df = pd.read_csv("data/mock_sap_data.csv")
    assert (df["amount"] >= 0).all()

def test_required_columns_exist():
    expected_cols = {"Date", "Product", "Amount", "Region"}
    df = pd.read_csv("data/mock_sap_data.csv")
    assert expected_cols.issubset(df.columns)

