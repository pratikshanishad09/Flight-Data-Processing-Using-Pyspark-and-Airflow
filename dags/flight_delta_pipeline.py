from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    dag_id='retail_delta_etl_pipeline',
    default_args=default_args,
    description='Run PySpark job to process retail data and save as Delta table',
    schedule_interval='@daily',
    start_date=datetime(2025, 5, 21),
    catchup=False,
) as dag:

    run_spark_job = BashOperator(
        task_id='run_spark_etl',
        bash_command='spark-submit /opt/airflow/dags/retail_etl.py'
    )
