
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount
from datetime import datetime

default_args = {
    'start_date': datetime(2019, 1, 1)
}

with DAG('batch_flight_pipeline',
         default_args=default_args,
         schedule_interval='@quarterly',
         catchup=False) as dag:

    run_spark = DockerOperator(
        task_id='run_spark_processing',
        image='bitnami/spark:latest',
        api_version='auto',
        auto_remove=True,
        command='/opt/bitnami/spark/bin/spark-submit /spark/batch_processing.py',
        docker_url='unix://var/run/docker.sock',
        network_mode='bridge',
        mounts=[
            Mount(source='/home/vboxuser/Desktop/BatchProcessing/spark',  # absolute path on host
                  target='/spark',  # mount path in container
                  type='bind'),
            Mount(source='/home/vboxuser/Desktop/data', target='/data', type='bind'),
        ],
        )

