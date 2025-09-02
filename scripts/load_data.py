import duckdb
import os

# Paths
db_path = os.path.join("data", "india_jobs.duckdb")
csv_path = os.path.join("data", "india_jobs_dataset.csv")

# Connect to (or create) DuckDB database file
con = duckdb.connect(db_path)

# Create table from CSV (overwrite if exists)
con.execute("DROP TABLE IF EXISTS india_jobs;")
con.execute(f"""
    CREATE TABLE india_jobs AS 
    SELECT * FROM read_csv_auto('{csv_path}')
""")

print("✅ Data loaded successfully into india_jobs table in", db_path)

# Quick sanity check
print(con.execute("SELECT COUNT(*) FROM india_jobs").fetchone())
