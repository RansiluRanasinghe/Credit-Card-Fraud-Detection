from fastapi import FastAPI, HTTPException
from App.schemas import FraudPredictionInput
from App.utils import load_modules, preprocess_inputs

app = FastAPI(title="Credit Card Fraud Detection API")

model = None
feature_names = None
scaler = None
THRESHOLD = 0.2

@app.on_event("startup")
def startup_event():
    global model, feature_names, scaler
    model, feature_names, scaler = load_modules()
    print("Model, Features, and Scaler loaded successfully.")

@app.get("/")
def home():
      return {"message": "Fraud Detection API is running. Send POST to /predict"}

@app.get("/healthz")
def health():
    return {"status": "ok", "model_loaded": model is not None}

@app.post("/predict")
def predict(payload: FraudPredictionInput):
     
     if not model:
          raise HTTPException(status_code=500, detail="Model not loaded")
     
     try:
          X_input = preprocess_inputs(payload, feature_names, scaler)

          prob_fraud = model.predict_proba(X_input)[0][1]

          is_fraud = (prob_fraud >= THRESHOLD)

          return{
               "probability": float(prob_fraud),
               "is_fraud": bool(is_fraud),
               "threshold_used": THRESHOLD,
               "decision": "DENY" if is_fraud else "APPROVE"
          }
     
     except ValueError as ve:
          raise HTTPException(status_code=400, detail=str(ve))
     except Exception as e:
          raise HTTPException(status_code=500, detail=str(e))
     
     