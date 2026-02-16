import pandas as pd
import re
import pickle

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from xgboost import XGBClassifier

# -------- CLEAN FUNCTION --------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# -------- LOAD DATA --------
df = pd.read_csv("mail_data.csv")
df.drop_duplicates(inplace=True)

df["Message"] = df["Message"].apply(clean_text)
df["Category"] = df["Category"].map({"ham":1, "spam":0})

X = df["Message"]
y = df["Category"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

# -------- PIPELINE --------
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(
        stop_words="english",
        ngram_range=(1,2)
    )),
    ("xgb", XGBClassifier(
        eval_metric="logloss",
        use_label_encoder=False
    ))
])

pipeline.fit(X_train, y_train)

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix,
    roc_auc_score
)

# -------- PREDICTIONS --------
y_pred = pipeline.predict(X_test)
y_prob = pipeline.predict_proba(X_test)[:,1]

# -------- METRICS --------
print("\n📊 MODEL EVALUATION\n")

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))
print("ROC-AUC:", roc_auc_score(y_test, y_prob))

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:\n")
print(confusion_matrix(y_test, y_pred))


# -------- SAVE --------
with open("model.pkl", "wb") as f:
    pickle.dump(pipeline, f)

print("✅ Model saved as model.pkl")
