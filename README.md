
#  Ask Your Data — LLM-Powered BI Assistant  

An interactive **Streamlit app** that allows users to query datasets in **natural language**.  
The app uses an **LLM (Groq’s LLaMA-3.1)** to generate SQL queries, executes them on a **DuckDB database**, and returns results as both a **table + chart**, along with a **one-sentence AI-generated insight**.  

---

##  Features
-  Ask questions in plain English → get **auto-generated SQL** queries  
-  Executes queries safely on **DuckDB** (no external server required)  
-  Interactive results: tables + **auto bar/line charts**  
-  AI-generated **summary insights** for each query  
-  Built-in **SQL validator** (blocks `DROP`, `DELETE`, etc.) for safety  

---

##  Project Structure
ask-your-data/
├─ data/
│  └─ india_jobs_dataset.csv     # sample dataset
├─ src/
│  ├─ llm_client.py              # LLM wrapper (Groq API)
│  ├─ db.py                      # DuckDB helpers
│  └─ sql_validator.py           # SQL validator
├─ scripts/
│  └─ load_data.py               # Load CSV → DuckDB
├─ app.py                        # Streamlit app entry point
├─ requirements.txt              # dependencies
├─ .env                          # API keys (NOT committed)
└─ README.md                     # this file
---

## ⚡ Setup & Run (macOS / Linux)

1. **Clone repo**
   ```bash
   git clone https://github.com/aasthagupta860/ask-your-data-bi-assistant.git
   cd ask-your-data-bi-assistant
   python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
GROQ_API_KEY=your_api_key_here
python scripts/load_data.py
streamlit run app.py
Open in browser:  http://localhost:8501
 Example Queries
	•	“Top 5 companies with the most job postings”
	•	“Average salary by location”
	•	“Show job postings in Bangalore with salary greater than 8 LPA”
	•	“How many jobs were posted in August 2025?”
	•	“Which company offers the highest average salary?”
    Tech Stack
	•	Python 3.13.5
	•	Streamlit → UI
	•	DuckDB → in-process analytical DB
	•	Groq LLaMA-3.1 API → LLM for text-to-SQL + summaries
	•	Altair → charts
	•	Pandas → dataframe handling

    Developed an LLM-powered BI Assistant in Python & Streamlit that converts natural language queries into SQL, executes them on DuckDB, and returns results as interactive tables, charts, and AI-generated summaries. Integrated Groq’s LLaMA-3.1 for inference with a secure SQL validation layer.

    Security Note
	•	Do not commit .env (API keys).
	•	Add .env to .gitignore.
	•	If an API key is exposed, revoke it immediately and generate a new one.

![Query Example](screenshots/query.png)
![Visualization](screenshots/chart.png)
