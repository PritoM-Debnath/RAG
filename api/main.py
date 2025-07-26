# api/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from app.rag import answer_query

app = FastAPI()

class QueryInput(BaseModel):
    question: str

@app.post("/query")
def query_api(input: QueryInput):
    answer = answer_query(input.question)
    return {"answer": answer}
