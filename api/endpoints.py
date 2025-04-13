import json
from rag.rag_engine import get_rag_answer
def get_analytics():
    with open("data/analytics_summary.json") as f: summary = json.load(f)
    return summary

def ask_question(query: str):
    return get_rag_answer(query)