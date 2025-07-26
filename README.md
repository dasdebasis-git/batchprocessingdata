<<<<<<< HEAD
# batchprocessingdata
batch processing of data for feeding into ML model
=======

# Batch Processing Architecture for Flight Delay Data

This project builds a containerized batch data processing pipeline using Kafka, HDFS, Spark, Airflow, and PostgreSQL.

## Prerequisites

- Docker
- Docker Compose
- Internet connection to pull Docker images

## Steps to Run

1. Download and extract flight delay dataset into `data/flight_delay_data.csv`.
2. Navigate to the `docker` folder and run:
   ```bash
   docker-compose up
   ```
3. Access Spark UI at `http://localhost:8080`, Airflow at `http://localhost:8081`, and PostgreSQL on port `5432`.
4. Trigger the DAG in Airflow to start the batch job.

## Output

Processed and aggregated flight delay data will be stored in the `flight_aggregates` table inside the PostgreSQL database.
>>>>>>> c2c2c4d (Initial commit - Batch processing project)
