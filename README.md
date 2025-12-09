#📌 Credit Card Fraud Detection — End-to-End ML + API Deployment

This project implements a complete fraud detection system using machine learning and deploys it as a production-grade API on Railway. It covers the full lifecycle of an ML application — from data preprocessing and model development to backend deployment and containerization.

Fraud detection is a high-impact real-world problem, and this project demonstrates how to build a practical, scalable solution using industry best practices.

⭐ Key Highlights

Trained a Random Forest model using a real-world credit card transactions dataset.

Applied robust evaluation metrics — precision, recall, F1-score, ROC-AUC — to handle highly imbalanced fraud data.

Implemented class imbalance techniques using class weighting and stratified splitting.

Built a clean FastAPI backend exposing a /predict endpoint for real-time fraud detection.

Packaged the model and API into a Docker container for reproducible deployment.

Deployed the API on Railway, offering a cloud-hosted, production-style inference service.

📂 Project Structure
Credit-Card-Fraud-Detection/
├── app/
│   ├── __init__.py
│   ├── main.py            # The API endpoints
│   ├── schemas.py         # Data validation (Pydantic)
│   ├── utils.py           # Preprocessing logic
│   └── model/
│       ├── rf_fraud_model.pkl
│       ├── model_features.pkl
│       └── scaler.pkl     # (Optional, see Step 0)
├── requirements.txt
└── README.md
└── .gitignore

🧠 What This Project Demonstrates
✔ End-to-End Machine Learning Workflow

Data loading & preprocessing

Exploratory analysis

Model training (Random Forest Classifier)

Evaluation using fraud-relevant metrics

Saving the trained model for inference

✔ Handling Imbalanced Fraud Data

Class weight adjustments

Stratified train-test split

Emphasis on recall & precision

✔ Production Backend

FastAPI for real-time predictions

Clean and documented /predict route

Pydantic model validation

✔ Deployment

Fully containerized with Docker

Railway hosting for scalable, cloud-based inference

Production-style API accessible via a public URL

🚀 Tech Stack
Layer	Technology
Model Development	Google Colab, Python, Pandas, Scikit-Learn
ML Model	Random Forest Classifier
Backend API	FastAPI
Deployment	Docker + Railway
Storage	Model pickle (model.pkl)
🔧 How to Run Locally
1. Clone the Repository
git clone https://github.com/<your-username>/Credit-Card-Fraud-Detection.git
cd Credit-Card-Fraud-Detection/backend

2. Install Dependencies
pip install -r requirements.txt

3. Start the API
uvicorn app:app --host 0.0.0.0 --port 8000

4. Test Locally

Visit:

http://localhost:8000/docs


You’ll see an interactive Swagger UI for prediction.

🐳 Run With Docker
Build the image:
docker build -t fraud-api -f docker/Dockerfile .

Run the container:
docker run -p 8000:8000 fraud-api

☁️ Deployment on Railway

The project is configured for one-click Railway deployment.

Railway Automatically Detects:

Dockerfile

Exposed port (8000)

FastAPI app

Once deployed, Railway provides a URL like:

https://credit-fraud-api-production.up.railway.app/predict


You can send JSON POST requests for predictions.

📊 Model Performance (Example)

(Replace with your actual numbers)

Metric	Score
Precision	0.92
Recall	0.86
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

🏆 Why This Project is Industry-Ready

Uses a real dataset with real fraud patterns.

Incorporates proper ML engineering standards.

Production-quality API design (FastAPI + Docker).

Cloud-hosted deployment (Railway).

Scalable and easily extendable for future work.

Perfect for LinkedIn posts, portfolios, and internship applications.