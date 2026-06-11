from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, col

spark = SparkSession.builder \
    .appName("Gold - Sales By Region") \
    .master("spark://spark-master:7077") \
    .config("spark.hadoop.fs.defaultFS", "hdfs://namenode:9000") \
    .getOrCreate()

df = spark.read.parquet("hdfs://namenode:9000/silver/superstore_clean")

df = df.withColumn("Sales", col("Sales").cast("double"))
df = df.na.fill({"Sales": 0})

result = df.groupBy("Region") \
    .agg(sum("Sales").alias("total_sales")) \
    .orderBy(col("total_sales").desc())

result.show()

result.write \
    .mode("overwrite") \
    .parquet("hdfs://namenode:9000/gold/sales_by_region")

spark.stop()