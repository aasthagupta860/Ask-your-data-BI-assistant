import os
from groq import Groq

def get_client():
    api_key = os.getenv("GROQ_API_KEY")
    return Groq(api_key=api_key)

def natural_language_to_sql(question: str, schema: str) -> str:
    client = get_client()
    messages = [
        {"role": "system", "content": "You are an expert SQL assistant. Output only valid SQL queries."},
        {"role": "user", "content": f"Schema: {schema}\nQuestion: {question}\nReturn ONLY SQL."}
    ]
    resp = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # 8B LLaMA 3 instant model
        messages=messages,
        max_tokens=256,
        temperature=0
    )
    return resp.choices[0].message.content.strip()

def summarize_results(question: str, df_sample_csv: str) -> str:
    client = get_client()
    messages = [
        {"role": "system", "content": "You are a data analyst. Write one short insight sentence."},
        {"role": "user", "content": f"Question: {question}\nResults sample:\n{df_sample_csv}"}
    ]
    resp = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        max_tokens=80,
        temperature=0.3
    )
    return resp.choices[0].message.content.strip()

