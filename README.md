# 📧 End-to-End Spam Detection System

An end-to-end Machine Learning project that detects whether a message is **Spam or Ham (Not Spam)** using NLP and XGBoost, deployed with a modern full-stack architecture.

This project demonstrates real-world ML workflow from model training to API deployment and frontend integration.

---

# 🚀 Live Demo

### 🌐 Streamlit Frontend  
👉 https://spam-detection-app-by-bala.streamlit.app/

### 🔗 FastAPI Backend  
👉 https://spam-detection-api-bq8l.onrender.com/docs

---

# 🎯 Project Objective

Spam emails and messages pose risks like phishing, fraud, and malware.  
This project builds a scalable system to classify messages as spam or ham in real time.

---

# 🧠 ML Approach

## Text Preprocessing
- Lowercasing
- URL removal
- Special character cleaning
- Whitespace normalization

## Feature Engineering
- TF-IDF Vectorization
- Unigrams + Bigrams

## Model
- XGBoost Classifier
- Implemented via Scikit-learn Pipeline

---

# 📊 Model Performance

| Metric | Score |
|--------|------|
| Accuracy | 97% |
| Precision | 97% |
| Recall (Ham) | 99% |
| Recall (Spam) | 80% |
| F1 Score | 98% |
| ROC-AUC | 0.97 |

Confusion Matrix:

```

[[103  25]
[  4 900]]

```

---

# 🏗 System Architecture

```

User Input
↓
Streamlit Frontend (UI)
↓
FastAPI Backend (API)
↓
ML Pipeline (TF-IDF + XGBoost)
↓
Prediction + Confidence Score


# ⚙️ How to Run Locally

## 1️⃣ Clone Repo

```

git clone https://github.com/Balusanu/Spam_Mail_Detection
cd spam-detection-system

```

---

## 2️⃣ Install Dependencies

Backend:

```

pip install -r backend/requirements.txt

```

Frontend:

```

pip install -r frontend/requirements.txt

```

---

## 3️⃣ Train Model (Optional)

```

python train.py

```

---

## 4️⃣ Run Backend API

```

uvicorn main:app --reload

```

---

## 5️⃣ Run Frontend

```

streamlit run app.py

```

---

# ☁️ Deployment

### Backend
- Deployed as FastAPI service
- Hosted on cloud platform
- REST API endpoints available

### Frontend
- Streamlit Cloud deployment
- Connected to live API

### CI/CD
- Auto-deploy enabled via GitHub integration

---

# ⚠️ Limitations

- Dataset based on older SMS/email spam corpus  
- May not capture modern phishing patterns  
- Real systems require periodic retraining  

---

# 🔮 Future Improvements

- Transformer models (DistilBERT)
- URL & domain reputation analysis
- Email header features
- Batch prediction endpoint
- Model monitoring & retraining pipeline
- User analytics dashboard

---

# 🛠 Tech Stack

### Machine Learning
- Python
- Scikit-learn
- XGBoost
- Pandas

### Backend
- FastAPI
- Uvicorn

### Frontend
- Streamlit

### DevOps
- GitHub
- Cloud deployment
- CI/CD pipelines

---

# 🌟 Key Learnings

✔ End-to-end ML deployment  
✔ API development with FastAPI  
✔ Frontend-backend integration  
✔ Model evaluation & tuning  
✔ Real-world ML architecture design  

---

# 👨‍💻 Author

**Balasubramanya C K**

If you found this project useful, consider ⭐ starring the repo!
