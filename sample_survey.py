import streamlit as st
import pandas as pd
from textblob import TextBlob
from collections import Counter
import re

# Store responses
if "responses" not in st.session_state:
    st.session_state.responses = []

st.title("NLP Survey Application")

st.write("Please answer the following questions.")

name = st.text_input("Name")

rating = st.slider("Overall Rating", 1, 5, 3)

feedback = st.text_area("Describe your experience")

submit = st.button("Submit")

def extract_keywords(text):
    words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())

    stopwords = {
        "this","that","with","have","were","been","from","your",
        "about","would","there","their","which","could","should",
        "very","really","just","more","than","when","what","where",
        "experience"
    }

    words = [w for w in words if w not in stopwords]

    return Counter(words).most_common(5)

if submit:

    sentiment = TextBlob(feedback).sentiment

    response = {
        "Name": name,
        "Rating": rating,
        "Feedback": feedback,
        "Polarity": sentiment.polarity,
        "Subjectivity": sentiment.subjectivity,
        "Keywords": extract_keywords(feedback)
    }

    st.session_state.responses.append(response)

    st.success("Survey Submitted!")

    st.write("### NLP Analysis")

    if sentiment.polarity > 0.2:
        st.success("Positive Feedback 😊")
    elif sentiment.polarity < -0.2:
        st.error("Negative Feedback 😞")
    else:
        st.info("Neutral Feedback 😐")

    st.write("Polarity:", round(sentiment.polarity,2))
    st.write("Subjectivity:", round(sentiment.subjectivity,2))

    st.write("Top Keywords")
    st.write(response["Keywords"])
