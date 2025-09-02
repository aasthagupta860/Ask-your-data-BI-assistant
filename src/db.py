"""
src/db.py
DuckDB helper functions
"""

import duckdb
import pandas as pd

DB_PATH = "data/india_jobs.duckdb"
TABLE_NAME = "india_jobs"

def get_connection():
    """Return a DuckDB connection to our DB file."""
    return duckdb.connect(DB_PATH, read_only=False)

def get_schema() -> str:
    """Return a string description of table schema (for LLM)."""
    con = get_connection()
    schema_df = con.execute(f"PRAGMA table_info({TABLE_NAME})").df()
    con.close()
    # Format into a readable string for LLM
    schema_str = ", ".join(
        f"{row['name']} ({row['type']})" for _, row in schema_df.iterrows()
    )
    return f"Table: {TABLE_NAME} Columns: {schema_str}"

def run_query(sql: str) -> pd.DataFrame:
    """Run SQL query against DuckDB and return DataFrame."""
    con = get_connection()
    try:
        df = con.execute(sql).df()
    finally:
        con.close()
    return df
