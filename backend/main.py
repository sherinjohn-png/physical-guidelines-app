from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pyodbc

app = FastAPI()

# ✅ Enable CORS so frontend (localhost:5173) can access API
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    "https://proud-pond-0423fb900.6.azurestaticapps.net",
    "http://localhost:5173"],  # Vue dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🎯 Root endpoint (just for testing)
@app.get("/")
def root():
    return {"message": "FastAPI backend is working!"}

# 🔐 Database credentials (consider loading from .env in future)
server = 'ie-project.database.windows.net'
database = 'iteration-1'
username = 'unionparty'
password = 'monash101!'
driver = '{ODBC Driver 18 for SQL Server}'

# 🔗 Connection string
conn_str = (
    f'DRIVER={driver};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password}'
)

@app.get("/guidelines")
def read_guidelines():
    try:
        with pyodbc.connect(conn_str) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM guidelines_summary")
            columns = [column[0] for column in cursor.description]
            results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return {"data": results}
    except Exception as e:
        return {"error": str(e)}

