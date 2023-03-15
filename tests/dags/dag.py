import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.python import PythonOperator

import logging
import sys

logger = logging.getLogger('airflow.task')
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
logger.addHandler(handler)

def test_log():
    print("\n\nHELLO WORLD!\n\n")

with DAG(
    'test_log',
    description='test log',
    schedule_interval=None,
    start_date=datetime.datetime(2022, 1, 19),
    catchup=False,
    tags=['log'],
) as dag:
    task = PythonOperator(
        task_id='test_log_task',
        python_callable=test_log,
        dag=dag
    )