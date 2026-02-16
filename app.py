import streamlit as st
import requests

# -------- CONFIG --------
st.set_page_config(
    page_title="Spam Detector",
    page_icon="📧",
    layout="centered"
)

API_URL = "https://spam-detection-api-bq8l.onrender.com/predict"

# -------- HEADER --------
st.title("📧 AI Spam Detector")
st.markdown(
    "Detect whether a message is **Spam or Ham** using ML."
)

# -------- SIDEBAR --------
st.sidebar.title("ℹ️ About")
st.sidebar.info(
"""
This app uses:

✅ TF-IDF + XGBoost  
✅ FastAPI backend  
✅ Real-time prediction  

Built for NLP portfolio projects.
"""
)

st.sidebar.markdown("---")
st.sidebar.write("**Tips:**")
st.sidebar.write("• Try scam messages")
st.sidebar.write("• Test work emails")
st.sidebar.write("• Mix short & long text")

# -------- EXAMPLES --------
st.subheader("✉️ Enter Message")

col1, col2 = st.columns(2)

if col1.button("📌 Spam Example"):
    st.session_state.msg = "Congratulations! You won ₹50,000. Claim now."

if col2.button("📌 Ham Example"):
    st.session_state.msg = "Hi team, meeting at 3 PM today."

msg = st.text_area(
    "Type or paste email text:",
    value=st.session_state.get("msg",""),
    height=150
)

# -------- PREDICT --------
if st.button("🔍 Analyze Message"):

    if not msg.strip():
        st.warning("⚠️ Please enter a message")
    else:
        with st.spinner("Analyzing..."):

            try:
                res = requests.post(
                    API_URL,
                    json={"message": msg}
                )

                result = res.json()

                pred = result["prediction"]
                conf = result["confidence"]

                st.markdown("---")

                # -------- RESULT --------
                if pred == "Spam":
                    st.error(f"🚫 **SPAM DETECTED**")
                    st.progress(min(conf,1.0))
                else:
                    st.success(f"✅ **HAM (Safe Message)**")
                    st.progress(min(conf,1.0))

                st.write(f"**Confidence:** {conf:.2%}")

            except:
                st.error("⚠️ API not reachable")

# -------- FOOTER --------
st.markdown("---")
st.caption("Built with ❤️ using Streamlit + FastAPI")
