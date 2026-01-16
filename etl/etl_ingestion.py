"""
Purpose:
- Ingest SAP and operational data
- Load into BigQuery staging tables
"""

import pandas as pd
from google.cloud import bigquery
from google.cloud.exceptions import GoogleCloudError

PROJECT_ID = "my_project"
DATASET = "staging"

def load_to_bigquery(df, table_name):
    client = bigquery.Client(project=PROJECT_ID)
    table_id = f"{PROJECT_ID}.{DATASET}.{table_name}"

    job = client.load_table_from_dataframe(
        df,
        table_id,
        job_config=bigquery.LoadJobConfig(
            write_disposition="WRITE_APPEND"
        )
    )
    job.result()
    print(f"Loaded {len(df)} records into {table_name}")

def ingest_sap():
    df = pd.read_csv("../data/mock_sap_data.csv")
    load_to_bigquery(df, "source_sap_finance")

def ingest_operations():
    df = pd.read_csv("../data/mock_operations_data.csv")
    load_to_bigquery(df, "source_operations")

if __name__ == "__main__":
    try:
        ingest_sap()
        ingest_operations()
        print("ETL ingestion completed successfully.")
    except GoogleCloudError as e:
        print(f"ETL failed: {e}")
