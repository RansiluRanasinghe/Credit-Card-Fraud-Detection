📌 Credit Card Fraud Detection — End-to-End ML + FastAPI Application

This project implements a complete credit card fraud detection system built using machine learning and served through a FastAPI backend. It covers the core workflow of a real ML application — from data preprocessing and model training to backend integration — while keeping the system simple, reproducible, and industry-aligned.

Fraud detection is a high-impact domain where minimizing false negatives is critical, and this project demonstrates practical techniques for handling highly imbalanced data.

⭐ Key Highlights

Trained a Random Forest model using a real-world credit card transactions dataset.

Applied evaluation metrics optimized for fraud detection: precision, recall, F1-score, ROC-AUC.

Addressed class imbalance using class weighting and stratified sampling.

Built a clean FastAPI backend exposing a /predict endpoint for real-time inference.

Saved model artifacts (model.pkl, model_features.pkl) for reproducible prediction.

Fully runnable locally with Uvicorn — no cloud deployment required.

Organized project structure following ML engineering best practices.

📂 Project Structure
Credit-Card-Fraud-Detection/
├── app/
│   ├── __init__.py
│   ├── main.py              # API routes
│   ├── schemas.py           # Pydantic input model
│   ├── utils.py             # Preprocessing + prediction logic
│   └── model/
│       ├── rf_fraud_model.pkl
│       └── model_features.pkl
├── requirements.txt
├── .gitignore
└── README.md

🧠 What This Project Demonstrates
✔ End-to-End Machine Learning

Data loading & preprocessing

Exploratory analysis

Random Forest training

Evaluation with fraud-focused metrics

Saving the trained model for inference

✔ Handling Imbalanced Data

Class weighting

Stratified train-test split

Threshold tuning for higher recall

✔ Backend Integration

FastAPI for real-time inference

/predict endpoint with Pydantic validation

Model + feature-order consistency

✔ Local Production Simulation

Run a real API server via Uvicorn

Test the model through Swagger UI

This makes the project ready for portfolios, internships, and LinkedIn posts.

🚀 Tech Stack
Layer	Technology
Model Development	Google Colab, Pandas, Scikit-Learn
ML Model	Random Forest Classifier
Backend API	FastAPI
Runtime	Uvicorn
Storage	Pickle model artifacts
🔧 How to Run Locally
1. Clone the Repository
git clone https://github.com/<your-username>/Credit-Card-Fraud-Detection.git
cd Credit-Card-Fraud-Detection

2. Create and Activate Virtual Environment (Windows)
python -m venv venv
venv\Scripts\activate


(For Linux/Mac)

source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Start the API
uvicorn app.main:app --reload

5. Open Swagger UI

Visit:

👉 http://localhost:8000/docs

You can test predictions directly from the browser.

📊 Model Performance (Example — replace with your numbers)
Metric	Score
Precision	1.00
Recall	0.80
F1 Score	0.89
ROC-AUC	0.99
🧪 Example Prediction Request
POST /predict
{
  "V1": -1.359807,
  "V2": -0.072781,
  "V3": 2.536347,
  "V4": 1.378155,
  "V5": -0.338321,
  "Amount": 149.62
}

Response
{
  "fraud": 0,
  "confidence": 0.12
}
