import streamlit as st
import pandas as pd
from textblob import TextBlob
from collections import Counter
import re
from textblob import Word


st.subheader("Sentiment Analysis")
str = "Python is amazing!"
st.write(str)
blob = TextBlob(str)
st.write(blob.sentiment)
st.markdown("---")

st.subheader("Words and Sentences")
str = "Python is amazing!"
st.write(str)
blob = TextBlob(str)
st.write(blob.words)
st.write(blob.sentences)
st.markdown("---")

