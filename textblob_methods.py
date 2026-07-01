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
print(blob.sentiment)
st.markdown("---")

