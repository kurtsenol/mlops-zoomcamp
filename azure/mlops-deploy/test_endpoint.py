import os
import json
import time
import requests
from dotenv import load_dotenv

# Load credentials
load_dotenv()
url = os.getenv("SCORING_URI")
key = os.getenv("SCORING_KEY")

if not url or not key:
    raise EnvironmentError("Missing SCORING_URI or SCORING_KEY in .env")

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {key}"
}

# Sample batch payload (you can change or load from file)
sample_data = [
    {"PU_DO": "129_205", "trip_distance": 3.5},
    {"PU_DO": "132_148", "trip_distance": 12.7},
    {"PU_DO": "230_265", "trip_distance": 1.2}
]

payload = {"data": sample_data}

def invoke_endpoint(data):
    try:
        start = time.time()
        response = requests.post(url, headers=headers, data=json.dumps(data), timeout=10)
        duration = time.time() - start

        response.raise_for_status()
        print(f"✅ Response time: {duration:.2f}s")
        print(f"📦 Predictions: {response.json()}")
    except requests.exceptions.HTTPError as http_err:
        print(f"❌ HTTP error: {http_err}")
        print("🔎 Response:", response.text)
    except Exception as err:
        print(f"❌ Unexpected error: {err}")

if __name__ == "__main__":
    invoke_endpoint(payload)
