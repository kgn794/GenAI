from textblob import TextBlob
from textblob import Word
import streamlit as st

st.subheader("Sentiment Analysis")
str = "Python is amazing!"
st.write(str)
blob = TextBlob(str)
print(blob.sentiment)
st.markdown("---")

st.subheader("Words and Sentences")
str = "Python is amazing!"
st.write(str)
blob = TextBlob(str)
print(blob.words)
print(blob.sentences)
st.markdown("---")

st.subheader("Tags")
str = "I love Python"
st.write(str)
blob = TextBlob(str)
print(blob.tags)
st.markdown("---")

st.subheader("Correct")
str = "I havv a dreem"
st.write(str)
blob = TextBlob(str)
print(blob.correct())
st.markdown("---")

st.subheader("Noun Phrases")
str = "Machine learning is a branch of artificial intelligence."
st.write(str)
blob = TextBlob(str)
print(blob.noun_phrases)
st.markdown("---")

st.subheader("Word Counts")
str = "apple apple mango"
st.write(str)
blob = TextBlob(str)
print(blob.word_counts)
st.markdown("---")

st.subheader("Spell Check")
str = "pythn"
st.write(str)
blob = TextBlob(str)
print(blob.words[0].spellcheck())
st.markdown("---")

st.subheader("NGrams")
str = "I love Python programming"
st.write(str)
blob = TextBlob(str)
print(blob.ngrams(2))
st.markdown("---")

st.subheader("Translate")
str = "Hello"
st.write(str)
blob = TextBlob(str)
translated = blob.translate(
    from_lang="en",
    to="fr"
)
print(translated)
st.markdown("---")

st.subheader("Detect Language")
str = "Hello, how are you?"
st.write(str)
blob = TextBlob(str)
print(blob.detect_language())
st.markdown("---")

st.subheader("Stemming")
str = "running"
st.write(str)
print(Word(str).stem())
st.markdown("---")

st.subheader("Lemmatize - As Verb")
str = "running"
st.write(str)
word = Word(str)
print(word.lemmatize("v"))
st.markdown("---")

st.subheader("Lemmatize")
st.write("cars and children")
print(Word("cars").lemmatize())
print(Word("children").lemmatize())
st.markdown("---")

st.subheader("Lemmatize - As Adjective")
str = "better"
st.write(str)
print(Word(str).lemmatize("a"))
st.markdown("---")

st.subheader("Pluralize")
str = "car"
st.write(str)
word = Word(str)
print(word.pluralize())
st.markdown("---")

st.subheader("Singularize")
str = "cars"
st.write(str)
word = Word(str)
print(word.singularize())
st.markdown("---")

st.subheader("Raw Format")
str = "John is reading a Python book."
st.write(str)
blob = TextBlob(str)
print(blob.raw)
st.markdown("---")

st.subheader("Parse the Words")
st.write(str)
print(blob.parse())
st.markdown("---")

st.subheader("Json Format")
st.write(str)
print(blob.json)
st.markdown("---")
