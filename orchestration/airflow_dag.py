from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
from datetime import datetime

default_args = {
    "owner": "data-engineering",
    "start_date": datetime(2026, 1, 1),
    "retries": 1,
}

with DAG(
    dag_id="sap_ops_etl_pipeline",
    schedule_interval="0 2 * * *",
    default_args=default_args,
    catchup=False,
) as dag:

    ingest_data = BashOperator(
        task_id="ingest_data",
        bash_command="python etl/etl_ingestion.py"
    )

    transform_data = BigQueryInsertJobOperator(
        task_id="transform_data",
        configuration={
            "query": {
                "query": open("etl/etl_transformations.sql").read(),
                "useLegacySql": False,
            }
        },
    )

    ingest_data >> transform_data

