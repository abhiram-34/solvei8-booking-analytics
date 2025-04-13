from fastapi import FastAPI
from pydantic import BaseModel
from api.endpoints import get_analytics, ask_question

app = FastAPI()
class AskInput(BaseModel):
    question: str
@app.post("/analytics")
def analytics():
    return get_analytics()
@app.post("/ask")
def ask(input: AskInput):
    answer = ask_question(input.question)
    return {"answer": answer}