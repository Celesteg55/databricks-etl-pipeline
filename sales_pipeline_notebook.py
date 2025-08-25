# Databricks-Style Notebook Simulation

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, month, year, sum as _sum

# Start Spark session
spark = SparkSession.builder.appName("SalesforcePipelineSimulation").getOrCreate()

# Load raw sales data (mock JSON)
df = spark.read.json("data/raw_sales.json")

# Clean data
df_clean = df.na.drop(subset=["customer_id", "amount"])

# Add year/month columns
df_clean = df_clean.withColumn("date", to_date(col("date"), "yyyy-MM-dd"))
df_clean = df_clean.withColumn("year", year(col("date")))
df_clean = df_clean.withColumn("month", month(col("date")))

# Aggregate sales per customer per month
sales_summary = df_clean.groupBy("customer_id", "year", "month") \
    .agg(_sum("amount").alias("total_sales"))

# Save as Parquet (Delta Lake simulation)
sales_summary.write.mode("overwrite").parquet("outputs/cleaned_sales.parquet")

# Save to CSV (Power BI-ready)
sales_summary.toPandas().to_excel("outputs/sales_summary.xlsx", index=False)

print("✅ Pipeline complete: Data saved to outputs/")
