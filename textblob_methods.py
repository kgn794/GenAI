import streamlit as st
import pandas as pd
from textblob import TextBlob
from collections import Counter
import re
from textblob import Word
import ssl
import nltk

nltk.set_proxy('http://proxy.company.com:8080')

nltk.download('brown')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('conll2000')
nltk.download('movie_reviews')

st.subheader("Sentiment Analysis")
str = "Python is amazing!"
st.write(str)
blob = TextBlob(str)
st.write(blob.sentiment)
st.markdown("---")

st.subheader("Tags")
str = "I love Python"
st.write(str)
blob = TextBlob(str)
print(blob.tags)
st.markdown("---")
