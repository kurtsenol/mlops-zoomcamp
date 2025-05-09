import json
import pickle
import numpy as np
from azureml.core.model import Model

def init():
    global model
    global dv

    model_path = Model.get_model_path("nyc-taxi-best-model")
    with open(model_path, "rb") as f:
        model = pickle.load(f)

    dv_path = Model.get_model_path("nyc-taxi-preprocessor")
    with open(dv_path, "rb") as f:
        dv = pickle.load(f)

def run(raw_data):
    try:
        data = json.loads(raw_data)["data"]
        X = dv.transform(data)
        preds = model.predict(X)
        return preds.tolist()
    except Exception as e:
        return str(e)
