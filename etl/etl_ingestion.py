"""
Ingest SAP and operational CSV data into BigQuery staging tables.
"""

import pandas as pd
from google.cloud import bigquery

PROJECT_ID = "my_project"
DATASET = "staging"

def load_csv_to_bq(csv_path, table_name):
    client = bigquery.Client(project=PROJECT_ID)
    df = pd.read_csv(csv_path)

    table_id = f"{PROJECT_ID}.{DATASET}.{table_name}"

    job = client.load_table_from_dataframe(
        df,
        table_id,
        job_config=bigquery.LoadJobConfig(
            write_disposition="WRITE_APPEND"
        )
    )
    job.result()
    print(f"Loaded {len(df)} rows into {table_name}")

if __name__ == "__main__":
    load_csv_to_bq("../data/mock_sap_finance.csv", "source_sap_finance")
    load_csv_to_bq("../data/mock_operations.csv", "source_operations")
