"""Spark processing pipeline."""
import os
import logging
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, udf
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_spark(app_name: str = "data_pipeline", master: str = "local[4]"):
    spark = (
        SparkSession.builder.appName(app_name)
        .master(master)
        .config("spark.sql.adaptive.enabled", "true")
        .getOrCreate()
    )
    logger.info(f"Spark session created with master={master}")
    return spark

def load_raw(spark, raw_path: str = "data/raw"):
    """Load all CSV files in raw_path."""
    import glob
    csv_files = glob.glob(os.path.join(raw_path, "*.csv"))
    if not csv_files:
        raise FileNotFoundError(f"No CSV files found at {raw_path}")
    df = spark.read.option("header", "true").option("inferSchema", "true").csv(csv_files)
    logger.info(f"Loaded {df.count()} rows from raw CSVs")
    return df

def clean(df):
    """Basic cleaning: drop duplicates, fill missing values."""
    df_clean = df.dropDuplicates()
    for col_name in df.columns:
        if df.schema[col_name].dataType in (IntegerType(), DoubleType()):
            df_clean = df_clean.fillna(0, subset=[col_name])
        else:
            df_clean = df_clean.fillna("unknown", subset=[col_name])
    return df_clean

def engineer_features(df):
    """Add example engineered features."""
    # Example: compute engagement score if retweet_count or reply_count exist
    if "retweet_count" in df.columns and "reply_count" in df.columns:
        df = df.withColumn(
            "engagement_score",
            (col("retweet_count") + col("reply_count")) * 0.5,
        )
    # Example: text length (if text column exists)
    if "text" in df.columns:
        df = df.withColumn("text_length", f.length(col("text")))
    return df

def write_features(df, output_path="data/processed/features.parquet"):
    df.write.mode("overwrite").parquet(output_path)
    logger.info(f"Features written to {output_path}")

def main():
    spark = create_spark()
    try:
        raw_df = load_raw(spark)
        cleaned_df = clean(raw_df)
        feat_df = engineer_features(cleaned_df)
        write_features(feat_df)
    finally:
        spark.stop()

if __name__ == "__main__":
    main()