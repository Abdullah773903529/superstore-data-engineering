from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date

spark = SparkSession.builder \
    .appName("BronzeToSilver") \
    .getOrCreate()

# Read from HDFS
df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv("hdfs:///bronze/superstore.csv")

print("Original Schema")
df.printSchema()

# Convert dates
df = df.withColumn("Order Date", to_date(col("Order Date"), "M/d/yyyy")) \
       .withColumn("Ship Date", to_date(col("Ship Date"), "M/d/yyyy"))

# FIX DATA TYPES (important)
df = df.withColumn("Sales", col("Sales").cast("double")) \
       .withColumn("Quantity", col("Quantity").cast("int")) \
       .withColumn("Discount", col("Discount").cast("double"))

# Clean data
df = df.dropna()
df = df.dropDuplicates()

print("Cleaned Schema")
df.printSchema()

# Write to Silver (optimized)
df.write \
    .mode("overwrite") \
    .partitionBy("Region") \
    .parquet("hdfs:///silver/superstore_clean")

print("SUCCESS: Data written to Silver Layer")

spark.stop()