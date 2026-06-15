"""PostgreSQL data extraction."""

import os
import pandas as pd
import psycopg2
from src import config

def get_connection():
    """Create a PostgreSQL connection using credentials from config."""
    return psycopg2.connect(
        host=config.config["database"]["host"],
        port=config.config["database"]["port"],
        dbname=config.config["database"]["name"],
        user=config.config["database"]["user"],
        password=config.config["database"]["password"],
    )

def extract_table(table_name: str) -> pd.DataFrame:
    """Extract an entire table into a pandas DataFrame."""
    conn = get_connection()
    try:
        df = pd.read_sql(f"SELECT * FROM {table_name}", conn)
    finally:
        conn.close()
    return df

def run_query(query: str) -> pd.DataFrame:
    """Execute a custom SQL query and return the result as a DataFrame."""
    conn = get_connection()
    try:
        df = pd.read_sql(query, conn)
    finally:
        conn.close()
    return df