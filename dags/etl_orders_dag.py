from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from scripts.transform_orders import transform_orders_data

with DAG(
    dag_id="etl_orders_pipeline",
    start_date=datetime(2024,1,1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    transform_orders = PythonOperator(
        task_id="transform_orders",
        python_callable=transform_orders_data
    )
