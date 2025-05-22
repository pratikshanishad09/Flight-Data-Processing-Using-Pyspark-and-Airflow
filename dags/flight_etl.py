from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Retail Delta ETL") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()

df = spark.read.csv("file:///opt/airflow/dags/clean_dataset.csv", header=True, inferSchema=True)

# Example transformation: convert price to integer
df = df.withColumn("price", df["price"].cast("int"))

# Save as Delta
df.write.format("delta").mode("overwrite").save("file:///opt/airflow/dags/delta/retail_data")
