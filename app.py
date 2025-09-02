import streamlit as st
import pandas as pd
import altair as alt
from dotenv import load_dotenv
import os

# Force load from project root
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))



from src.llm_client import natural_language_to_sql, summarize_results
from src.sql_validator import validate_sql
from src import db

st.set_page_config(page_title="Ask Your Data", layout="wide")

st.title("🤖 Ask Your Data — LLM-Powered BI Assistant")

# Sidebar
st.sidebar.header("Settings")
show_schema = st.sidebar.checkbox("Show Table Schema")

# Step 1: Show schema
schema = db.get_schema()
if show_schema:
    st.sidebar.text(schema)

# Step 2: User input
question = st.text_input("Ask a question about your jobs dataset:")

if question:
    st.write(f"**Your Question:** {question}")

    # Step 3: NL -> SQL
    with st.spinner("🔍 Generating SQL..."):
        sql = natural_language_to_sql(question, schema)

    st.code(sql, language="sql")

    # Step 4: Validate SQL
    try:
        sql = validate_sql(sql)
    except Exception as e:
        st.error(f"❌ Invalid SQL generated: {e}")
        st.stop()

    # Step 5: Run query
    try:
        df = db.run_query(sql)
    except Exception as e:
        st.error(f"❌ Query failed: {e}")
        st.stop()

    if df.empty:
        st.warning("⚠️ Query returned no results.")
        st.stop()

    # Step 6: Show results
    st.subheader("📊 Results")
    st.dataframe(df)

    # Step 7: Chart (auto bar/line)
    try:
        if df.shape[1] >= 2:
            x, y = df.columns[0], df.columns[1]
            chart = alt.Chart(df).mark_bar().encode(x=x, y=y)
            st.altair_chart(chart, use_container_width=True)
    except Exception:
        st.info("Could not auto-generate chart.")

    # Step 8: Summarize
    sample_csv = df.head(5).to_csv(index=False)
    with st.spinner("✍️ Generating summary..."):
        summary = summarize_results(question, sample_csv)
    st.success(summary)
