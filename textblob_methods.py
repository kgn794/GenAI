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

st.subheader("Tags")
str = "I love Python"
st.write(str)
blob = TextBlob(str)
st.write(blob.tags)
st.markdown("---")

st.subheader("Correct")
str = "I havv a dreem"
st.write(str)
blob = TextBlob(str)
st.write(blob.correct())
st.markdown("---")

st.subheader("Noun Phrases")
str = "Machine learning is a branch of artificial intelligence."
st.write(str)
blob = TextBlob(str)
st.write(blob.noun_phrases)
st.markdown("---")

st.subheader("Word Counts")
str = "apple apple mango"
st.write(str)
blob = TextBlob(str)
st.write(blob.word_counts)
st.markdown("---")

st.subheader("Spell Check")
str = "pythn"
st.write(str)
blob = TextBlob(str)
st.write(blob.words[0].spellcheck())
st.markdown("---")

st.subheader("NGrams")
str = "I love Python programming"
st.write(str)
blob = TextBlob(str)
st.write(blob.ngrams(2))
st.markdown("---")

st.subheader("Translate")
str = "Hello"
st.write(str)
blob = TextBlob(str)
translated = blob.translate(
    from_lang="en",
    to="fr"
)
st.write(translated)
st.markdown("---")

st.subheader("Detect Language")
str = "Hello, how are you?"
st.write(str)
blob = TextBlob(str)
st.write(blob.detect_language())
st.markdown("---")

st.subheader("Stemming")
str = "running"
st.write(str)
st.write(Word(str).stem())
st.markdown("---")

st.subheader("Lemmatize - As Verb")
str = "running"
st.write(str)
word = Word(str)
st.write(word.lemmatize("v"))
st.markdown("---")

st.subheader("Lemmatize")
st.write("cars and children")
st.write(Word("cars").lemmatize())
st.write(Word("children").lemmatize())
st.markdown("---")

st.subheader("Lemmatize - As Adjective")
str = "better"
st.write(str)
st.write(Word(str).lemmatize("a"))
st.markdown("---")

st.subheader("Pluralize")
str = "car"
st.write(str)
word = Word(str)
st.write(word.pluralize())
st.markdown("---")

st.subheader("Singularize")
str = "cars"
st.write(str)
word = Word(str)
st.write(word.singularize())
st.markdown("---")

st.subheader("Raw Format")
str = "John is reading a Python book."
st.write(str)
blob = TextBlob(str)
st.write(blob.raw)
st.markdown("---")

st.subheader("Parse the Words")
st.write(str)
st.write(blob.parse())
st.markdown("---")

st.subheader("Json Format")
st.write(str)
st.write(blob.json)
st.markdown("---")
