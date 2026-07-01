import streamlit as st
import pandas as pd
import numpy as np
import time

st.title("Survey Application")
st.header("Customer Feedback")
st.subheader("Enter your response")
st.text("Plain text")
st.write("Hello Streamlit")
st.markdown("**Bold Text**")
st.code("print('Hello')")
st.latex(r"E = mc^2")

name = st.text_input("Enter Name")
feedback = st.text_area("Feedback")
age = st.number_input("Age", 18, 100)
rating = st.slider("Rating", 1, 5, 3)
city = st.selectbox(
    "City",
    ["Chennai", "Delhi", "Mumbai"]
)
skills = st.multiselect(
    "Skills",
    ["Python", "Java", "C++"]
)
gender = st.radio(
    "Gender",
    ["Male", "Female"]
)
agree = st.checkbox("I Agree")
if st.button("Submit"):
    st.success("Submitted")

file = st.file_uploader(
    "Upload File",
    type=["csv", "jpg", "png"]
)

df = pd.DataFrame({
    "Name":["John","Mary"],
    "Age":[22,25]
})

st.table(df)
st.dataframe(df)
st.json({
    "Name":"John",
    "Age":25
})

data = pd.DataFrame(
    np.random.randn(20,3),
    columns=["A","B","C"]
)

st.line_chart(data)
st.bar_chart(data)
st.area_chart(data)

bar = st.progress(0)

for i in range(100):
    time.sleep(0.05)
    bar.progress(i+1)

with st.spinner("Loading..."):
    time.sleep(3)

st.success("Success")
st.error("Error")
st.warning("Warning")
st.info("Information")

col1, col2 = st.columns(2)

with col1:
    st.button("Left")

with col2:
    st.button("Right")


st.sidebar.title("Menu")

option = st.sidebar.selectbox(
    "Choose",
    ["Home","About"]
)

tab1, tab2 = st.tabs(
    ["Home","About"]
)

with tab1:
    st.write("Home Page")

with tab2:
    st.write("About Page")


with st.expander("Show Details"):
    st.write("Hidden content")

with st.form("login"):

    username = st.text_input("Username")
    password = st.text_input(
        "Password",
        type="password"
    )

    submit = st.form_submit_button("Login")

container = st.container()

with container:
    st.write("Inside Container")

placeholder = st.empty()

placeholder.write("Loading...")

placeholder.write("Completed")

st.download_button(
    "Download",
    data="Hello",
    file_name="hello.txt"
)

st.metric(
    "Revenue",
    "$50,000",
    "+15%"
)

if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Increment"):
    st.session_state.count += 1

st.write(st.session_state.count)

st.balloons()

st.snow()

st.set_page_config(
    page_title="My App",
    page_icon="📊",
    layout="wide"
)
