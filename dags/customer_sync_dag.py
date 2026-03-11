from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from scripts.fetch_customer_api import fetch_customer_data

with DAG(
    dag_id="customer_sync_pipeline",
    start_date=datetime(2024,1,1),
    schedule_interval="@hourly",
    catchup=False
) as dag:

    fetch_customers = PythonOperator(
        task_id="fetch_customer_api",
        python_callable=fetch_customer_data
    )
