# score.py
import json
import pickle
import numpy as np
from scipy import sparse

def init():
    global model
    global dv

    with open("model.pkl", "rb") as f:
        model = pickle.load(f)

    with open("dv.b", "rb") as f:
        dv = pickle.load(f)

def run(raw_data):
    try:
        data = json.loads(raw_data)["data"]
        X = dv.transform(data)
        preds = model.predict(X)
        return preds.tolist()
    except Exception as e:
        return {"error": str(e)}
