import requests
import time

API_URL = "http://127.0.0.1:8000"

start = time.time()
res_analytics = requests.post(f"{API_URL}/analytics")
end = time.time()
print("\n analytics Response")
print(f"Time: {(end - start):.2f} seconds")
print(f"Status Code: {res_analytics.status_code}")
print(f"Response: {res_analytics.json()}")
query = {"question": "What is the average ADR of bookings in Portugal?"}
start = time.time()
res_ask = requests.post(f"{API_URL}/ask", json=query)
end = time.time()
print("\n Ask Response")
print(f"Time: {(end - start):.2f} seconds")
print(f"Status Code: {res_ask.status_code}")
print(f"Answer: {res_ask.json()['answer']}")
