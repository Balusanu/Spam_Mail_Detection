from fastapi import FastAPI
from pydantic import BaseModel
import pickle

# -------- LOAD MODEL --------
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI(title="Spam Detection API")

class EmailRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"status": "Spam API running"}

@app.post("/predict")
def predict(req: EmailRequest):
    pred = model.predict([req.message])[0]
    prob = model.predict_proba([req.message])[0]

    return {
        "prediction": "Ham" if pred == 1 else "Spam",
        "confidence": float(max(prob))
    }
