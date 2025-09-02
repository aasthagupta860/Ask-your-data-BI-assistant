nano scripts/query_data.pynano scripts/qimport duckdb

DB_PATH = "data/india_jobs.duckdb"
TABLE_NAME = "india_jobs"

def main():
    con = duckdb.connect(DB_PATH)

    print("🔢 Total rows:", con.execute(f"SELECT COUNT(*) FROM {TABLE_NAME}").fetchone()[0])

    print("\n📊 Top 10 job titles:")
    print(con.execute(f"""
        SELECT job_title, COUNT(*) AS postings
        FROM {TABLE_NAME}
        GROUP BY job_title
        ORDER BY postings DESC
        LIMIT 10
    """).df())

    print("\n📍 Companies with most listings:")
    print(con.execute(f"""
        SELECT company_name, COUNT(*) AS postings
        FROM {TABLE_NAME}
        GROUP BY company_name
        ORDER BY postings DESC
        LIMIT 10
    """).df())

    con.close()

if __name__ == "__main__":
    main()
