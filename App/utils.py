import joblib
import pandas as pd
import numpy  as np
import os

MODEL_DIR = os.path.join(os.path.dirname(__file__), "model")

def load_modules():

    try:
        model_path = os.path.join(MODEL_DIR, "rf_fraud_model.pkl")
        features_path = os.path.join(MODEL_DIR, "model_features.pkl")
        scaler_path = os.path.join(MODEL_DIR, "scaler.pkl")

        model = joblib.load(model_path)
        features = joblib.load(features_path)

        try:
            scaler = joblib.load(scaler_path)
        except:
            scaler = None 

        return model, features, scaler
    except Exception as e:
        raise RuntimeError("Error loading modules: ", e)


def preprocess_inputs(input_data, feature_names, scaler = None):

    data = input_data.features.copy()

    raw_amount = input_data.amount
    if scaler:
        scaled_amount = scaler.transform([[raw_amount]])[0][0] 
    else:
        scaled_amount = (raw_amount - 88.35) / 250.12

    data["Amount_Scaled"] = scaled_amount

    try:
        orderd_data = [data[col] for col in feature_names]
    except KeyError as e:
        raise ValueError("Missing features: ", e)

    return np.array([orderd_data])        

