from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from bitso_challenge.load_csv_df import load_csv_df

default_args = {
    "owner": "Zuleima Quiroz",
    "depends_on_past": False,
    "start_date": datetime(2024, 4, 14),
    "retries": 1,
}

dag = DAG(
    "etl_pipeline",
    default_args=default_args,
    description="ETL pipeline with Airflow",
    schedule_interval="0 9 * * *",  # Run every day at 9 am
)


def run_etl():
    load_csv_df()


run_etl_task = PythonOperator(
    task_id="run_etl_task",
    python_callable=run_etl,
    dag=dag,
)

run_etl_task
