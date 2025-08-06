# classifier/app.py

import streamlit as st
import joblib

# Load trained model and vectorizer
model = joblib.load("models/model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

st.title("📰 News Topic Classifier")
st.write("Classify news articles based on their content using a TF-IDF + Naive Bayes model.")

# User input
user_input = st.text_area("Enter news text:")

if st.button("Classify"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        input_vector = vectorizer.transform([user_input])
        prediction = model.predict(input_vector)
        st.success(f"Predicted Topic: **{prediction[0]}**")
