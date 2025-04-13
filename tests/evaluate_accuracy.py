import json
import requests

with open("tests/test_queries.json") as f:
    queries = json.load(f)

correct = 0

for q in queries:
    res = requests.post("http://127.0.0.1:8000/ask", json={"question": q["question"]})
    answer = res.json()["answer"].lower()
    print(f"\nQ: {q['question']}\nA: {answer}")

    if all(word in answer for word in q["expected_keywords"]):
        correct += 1

print(f"\nAccuracy: {correct} / {len(queries)}")
