# End-to-End Data Science Pipeline

This repository contains a complete, functional project that demonstrates the following workflow:

1. **SQL Extraction** – Pull raw data from a PostgreSQL database.  
2. **Spark Processing** – Clean and engineer features using PySpark.  
3. **Machine Learning** – Train a custom PyTorch model with a bespoke loss function.  
4. **Model Deployment** – Serve the model via a FastAPI REST API.  
5. **User Interface** – Streamlit dashboard to trigger runs, monitor progress, and view results.  

The pipeline can collect data from major public sites (Twitter and Reddit) and process massive datasets in a distributed Spark environment.

---

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Configuration](#configuration)
- [Running the Pipeline](#running-the-pipeline)
- [Project Structure](#project-structure)
- [Acknowledgements](#acknowledgements)

---

## Prerequisites
- **PostgreSQL** instance (or compatible PostgreSQL‑compatible cloud service)  
- **Twitter** and **Reddit** API credentials (developer accounts)  
- **Apache Spark** (standalone or cluster mode)  
- **Python 3.11+**  
- **Git** (to clone the repository)

---

## Setup
```bash
# Clone the repo
git clone <repo-url>
cd data_pipeline

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## Configuration
Copy `config.yaml.template` to `config.yaml` and fill in your credentials:

```yaml
database:
  host: localhost
  port: 5432
  name: company_db
  user: db_user
  password: db_password

social:
  reddit:
    client_id: reddit_client_id
    client_secret: reddit_client_secret
    user_agent: reddit_user_agent
  twitter:
    bearer_token: twitter_bearer_token
```

---

## Running the Pipeline
### 1. Extract data from PostgreSQL
```bash
python -m src.extract.postgres_extractor
```

### 2. Ingest social media data
```bash
python -m src.ingest.twitter
python -m src.ingest.reddit
```

### 3. Process data with Spark
```bash
spark-submit src/processing/spark_processor.py
```

### 4. Train the custom model
```bash
python -m src.training.trainer
```

### 5. Save the trained model
The trainer automatically saves the model to `model.pt`.

### 6. Deploy the model API
```bash
uvicorn src.deploy.api:app --reload
```

### 7. Launch the UI
```bash
streamlit run ui/streamlit_app.py
```

Navigate to the Streamlit UI in your browser to trigger steps, monitor logs, and view results.

---

## Project Structure
```
data_pipeline/
├── README.md
├── requirements.txt
├── config.yaml
├── src/
│   ├── __init__.py
│   ├── extract/
│   │   ├── __init__.py
│   │   └── postgres_extractor.py
│   ├── ingest/
│   │   ├── __init__.py
│   │   ├── reddit.py
│   │   └── twitter.py
│   ├── processing/
│   │   ├── __init__.py
│   │   └── spark_processor.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── custom_model.py
│   ├── training/
│   │   ├── __init__.py
│   │   └── trainer.py
│   └── deploy/
│       ├── __init__.py
│       └── api.py
├── ui/
│   └── streamlit_app.py
└── run_pipeline.py
```

---

## Acknowledgements
- **PostgreSQL** – Robust relational database system.  
- **Apache Spark** – Distributed data processing engine.  
- **PyTorch** – Flexible deep‑learning framework.  
- **Streamlit** – Rapid UI development for data apps.  

---

Feel free to adapt the code to your specific use‑case, add more feature‑engineering steps, or expand the model architecture as needed. Happy coding! 