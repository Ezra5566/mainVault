"""Orchestrates the end‑to‑end data science pipeline.

The functions map directly to the modules we have created:
- src.extract.postgres_extractor
- src.ingest.twitter / reddit
- src.processing.spark_processor
- src.training.trainer
- src.deploy.api (model serving)
"""

import os
import subprocess
import sys
import logging
from pathlib import Path

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

# Project root (directory containing this script)
PROJECT_ROOT = Path(__file__).parent.resolve()

# Ensure required folders exist
DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_PROC = PROJECT_ROOT / "data" / "processed"
CHECKPOINTS = PROJECT_ROOT / "checkpoints"
MODEL_DIR = PROJECT_ROOT / "model"

for d in [DATA_RAW, DATA_PROC, CHECKPOINTS, MODEL_DIR]:
    d.mkdir(parents=True, exist_ok=True)

# ----------------------------------------------------------------------
# 1. Extract raw data from PostgreSQL
# ----------------------------------------------------------------------
def extract_from_postgres(table_name: str, out_path: Path):
    """Export an entire PostgreSQL table to a CSV file."""
    from src.extract.postgres_extractor import extract_table

    logger.info(f"Extracting table '{table_name}' from PostgreSQL → {out_path}")
    df = extract_table(table_name)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_path, index=False)
    logger.info(f"Extraction complete: {len(df)} rows saved")


# ----------------------------------------------------------------------
# 2. Ingest social media data
# ----------------------------------------------------------------------
def ingest_twitter(keyword: str = "climate change", max_tweets: int = 100):
    """Pull recent tweets and store as CSV."""
    from src.ingest.twitter import fetch_tweets

    logger.info(f"Ingesting tweets for keyword '{keyword}'")
    df = fetch_tweets(keyword, max_tweets=max_tweets)
    out_path = DATA_RAW / f"twitter_{keyword.replace(' ', '_')}.csv"
    df.to_csv(out_path, index=False)
    logger.info(f"Twitter ingestion complete: {len(df)} tweets saved to {out_path}")


def ingest_reddit(subreddit: str = "python", limit: int = 100):
    """Scrape top posts from a subreddit and store as CSV."""
    from src.ingest.reddit import fetch_posts

    logger.info(f"Ingesting Reddit posts from r/{subreddit}")
    df = fetch_posts(subreddit, limit=limit)
    out_path = DATA_RAW / f"reddit_{subreddit}.csv"
    df.to_csv(out_path, index=False)
    logger.info(f"Reddit ingestion complete: {len(df)} posts saved to {out_path}")


# ----------------------------------------------------------------------
# 3. Spark processing
# ----------------------------------------------------------------------
def run_spark_processing():
    """Execute the Spark job that cleans and engineers features."""
    spark_script = PROJECT_ROOT / "src" / "processing" / "spark_processor.py"
    logger.info(f"Launching Spark job: spark-submit {spark_script}")
    # Adjust master configuration here if you have a cluster
    master = "local[4]"
    cmd = [
        "spark-submit",
        spark_script,
    ]
    # If you set environment variables for Spark config, add them here
    logger.info(f"Executing: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        logger.error(f"Spark job failed:\n{result.stderr}")
        raise RuntimeError("Spark processing failed")
    logger.info("Spark processing completed successfully")


# ----------------------------------------------------------------------
# 4. Model training
# ----------------------------------------------------------------------
def train_model(
    epochs: int = 10,
    batch_size: int = 64,
    lr: float = 0.001,
    dropout: float = 0.3,
    hidden_dims: str = "128,64,32",
):
    """Run the PyTorch training routine."""
    logger.info(f"Starting model training (epochs={epochs}, batch_size={batch_size})")
    # Build the CLI arguments expected by trainer.trainer.main
    import subprocess

    env = os.environ.copy()
    cmd = [
        sys.executable,
        "-m",
        "src.training.trainer",
        f"--epochs={epochs}",
        f"--batch_size={batch_size}",
        f"--lr={lr}",
        f"--dropout={dropout}",
        f"--hidden_dims={hidden_dims}",
    ]
    logger.info(f"Running training command: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True, env=env)
    if result.returncode != 0:
        logger.error(f"Training script failed:\n{result.stderr}")
        raise RuntimeError("Model training failed")
    logger.info("Model training completed successfully")
    logger.info(f"Training output:\n{result.stdout}")


# ----------------------------------------------------------------------
# 5. Deploy the model (FastAPI)
# ----------------------------------------------------------------------
def start_api():
    """Launch the FastAPI server that serves predictions."""
    import uvicorn

    logger.info("Starting FastAPI server (uvicorn) …")
    # Run in background so Streamlit does not block; use a separate process
    cmd = ["uvicorn", "src.deploy.api:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
    logger.info(f"Running: {' '.join(cmd)}")
    # Using subprocess.Popen to keep the Streamlit UI responsive
    process = subprocess.Popen(cmd)
    return process


# ----------------------------------------------------------------------
# 6. Orchestrator entry‑point (optional CLI)
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run the full pipeline")
    parser.add_argument(
        "--step",
        choices=["extract", "ingest", "spark", "train", "deploy", "all"],
        default="all",
        help="Which part of the pipeline to execute",
    )
    args = parser.parse_args()

    if args.step in ["extract", "all"]:
        # Example: extract a placeholder table; replace with your actual table name
        extract_from_postgres(
            table_name="company_data", out_path=DATA_RAW / "extracted_table.csv"
        )
    if args.step in ["ingest", "all"]:
        ingest_twitter(keyword="climate change", max_tweets=50)
        ingest_reddit(subreddit="python", limit=30)
    if args.step in ["spark", "all"]:
        run_spark_processing()
    if args.step in ["train", "all"]:
        train_model(
            epochs=10,
            batch_size=64,
            lr=0.001,
            dropout=0.3,
            hidden_dims="128,64,32",
        )
    if args.step in ["deploy", "all"]:
        # Start the API in the background; it will keep running after this script exits
        api_proc = start_api()
        logger.info(f"FastAPI process started with PID {api_proc.pid}")
        # Keep the process alive for a short time so logs are visible
        import time

        time.sleep(5)
        api_proc.terminate()
        api_proc.wait()
        logger.info("FastAPI server stopped.")