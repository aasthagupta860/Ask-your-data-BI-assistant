"""
src/sql_validator.py
Improved SQL validator — allows only safe SELECT queries.
"""

def validate_sql(sql: str) -> str:
    # 🧹 Clean up: remove code fences if model included ```sql ... ```
    sql = sql.strip().replace("```sql", "").replace("```", "").strip()

    # 🧹 Remove trailing semicolons
    sql = sql.rstrip(";")

    # Lowercase version for checks
    sql_lower = sql.lower().lstrip()

    # ✅ Must start with SELECT
    if not sql_lower.startswith("select"):
        raise ValueError("❌ Only SELECT queries are allowed.")

    # ✅ Block dangerous keywords (to prevent table modifications)
    forbidden = ["drop", "delete", "update", "insert", "alter", "create"]
    for word in forbidden:
        if f" {word} " in f" {sql_lower} ":
            raise ValueError("❌ Forbidden SQL keyword detected.")

    # If passes all checks, return cleaned SQL
    return sql
