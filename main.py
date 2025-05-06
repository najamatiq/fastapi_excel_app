import pandas as pd
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

# Load Excel file
df = pd.read_excel("students.xlsx")

@app.get("/students")
def get_students():
    return JSONResponse(content=df.to_dict(orient="records"))
