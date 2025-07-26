
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, count, when, to_date, quarter

spark = SparkSession.builder.appName("FlightDelayBatchProcessing").getOrCreate()

df.write.format("csv").mode("overwrite").save("/data/output")
df = spark.read.option("header", True).csv("/data/flight_delay_data.csv")
df = df.dropna(subset=["FL_DATE", "AIRLINE", "ORIGIN", "ARR_DELAY", "CANCELLED"])

df = df.withColumn("flight_date", to_date(col("FL_DATE"), "yyyy-MM-dd"))
df = df.withColumn("quarter", quarter(col("flight_date")))

agg_df = df.groupBy("AIRLINE", "quarter").agg(
    avg(col("ARR_DELAY")).alias("avg_arrival_delay"),
    count(when(col("CANCELLED") == 1, True)).alias("total_cancellations"),
    count(when(col("ARR_DELAY") > 15, True)).alias("flights_delayed_over_15min")
)

agg_df.write.format("jdbc").options(
    url="jdbc:postgresql://postgres:5432/airflow",
    driver="org.postgresql.Driver",
    dbtable="flight_aggregates",
    user="airflow",
    password="airflow"
).mode("overwrite").save()
