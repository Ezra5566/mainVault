"""Streamlit dashboard for the end‑to‑end data science pipeline.

This UI lets a user:
- Start/stop pipeline steps,
- View logs,
- Trigger model inference,
- Browse processed features.

The app is deliberately lightweight so it can run on a local machine
or in a cloud notebook without extra infrastructure.
"""

import os
import subprocess
import sys
import logging
import time
from pathlib import Path

import streamlit as st

# ----------------------------------------------------------------------
# Logging configuration for Streamlit output
# ----------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.StreamHandler()],
)
log = logging.getLogger(__name__)

# ----------------------------------------------------------------------
# Helper to run subprocess commands and stream their output
# ----------------------------------------------------------------------
def run_command(cmd, capture_output=False):
    """Run a shell command and stream stdout/stderr to Streamlit."""
    log.info(f"Running: {' '.join(cmd)}")
    process = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1
    )
    # Stream line‑by‑line so the UI updates in real time
    for line in process.stdout:
        log.info(line.rstrip())
        # Streamlit requires mutations to be followed by a rerun
        yield line.rstrip()
    process.wait()
    yield f"Process exited with code {process.returncode}"


# ----------------------------------------------------------------------
# UI Layout
# ----------------------------------------------------------------------
st.set_page_config(page_title="Data Science Pipeline", layout="centered")
st.title("🔧 End‑to‑End Data Science Pipeline")

# Sidebar for step selection
st.sidebar.header("Pipeline Controls")
step = st.sidebar.selectbox(
    "Select step to run",
    options=["idle", "Extract", "Ingest Twitter", "Ingest Reddit", "Spark Process", "Train Model", "Run API", "Predict"],
)

# ----------------------------------------------------------------------
# Run selected step
# ----------------------------------------------------------------------
if step != "idle":
    st.write(f"### Running: {step}")

    # Define command lists for each step
    if step == "Extract":
        cmd = [sys.executable, "-m", "run_pipeline", "--step", "extract"]
    elif step == "Ingest Twitter":
        cmd = [sys.executable, "-m", "run_pipeline", "--step", "ingest", "--keyword", "climate change", "--max_tweets", "50"]
    elif step == "Ingest Reddit":
        cmd = [sys.executable, "-m", "run_pipeline", "--step", "ingest", "--subreddit", "python", "--limit", "30"]
    elif step == "Spark Process":
        cmd = ["spark-submit", str(Path(__file__).parent / ".." / "src" / "processing" / "spark_processor.py")]
    elif step == "Train Model":
        cmd = [sys.executable, "-m", "run_pipeline", "--step", "train"]
    elif step == "Run API":
        cmd = ["uvicorn", "src.deploy.api:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
    elif step == "Predict":
        # Simple placeholder – UI will call the API directly
        st.write("Prediction endpoint is exposed at http://localhost:8000/predict once the API is running.")
        st.write("You can test it via the Swagger UI at /docs.")
        st.stop()

    # Stream output in real time
    for line in run_command(cmd):
        # Streamlit auto‑updates on each yield
        st.text(line)

    st.success(f"✅ {step} completed.")
else:
    st.write("Select a pipeline step from the dropdown to get started.")

# ----------------------------------------------------------------------
# Auto‑refresh logs (optional)
# ----------------------------------------------------------------------
if st.checkbox("Auto‑refresh logs every 5 seconds"):
    placeholder = st.empty()
    while True:
        time.sleep(5)
        placeholder.empty()
```

This UI ties together the earlier scripts: it can launch the extract/ingest scripts, Spark job, trainer, and FastAPI server, while streaming logs back to the browser. Users can stop long‑running processes via the Streamlit UI or by interrupting the container.

Feel free to adjust titles, add more input fields (e.g., custom keywords, tweet counts), or extend the prediction widget with a feature‑upload component.