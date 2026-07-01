import streamlit as st
import pandas as pd
import numpy as np
import time


st.title("Title - title")
st.markdown("---")
st.header("Header - header")
st.subheader("Sub Header - subheader")
st.text("Plain text")
st.write("Normal text - write")
st.markdown("**Bold Text** - markdown")
st.code("print('Hello') - code")
st.latex(r"Formula text E = mc^2 - latex")

name = st.text_input("Enter Name - text_input")
feedback = st.text_area("Feedback - text_area")
age = st.number_input("Age - number_input", 18, 100)
rating = st.slider("Rating - slider", 1, 5, 3)
city = st.selectbox(
    "City - selectbox",
    ["Chennai", "Delhi", "Mumbai"]
)
skills = st.multiselect(
    "Skills - multiselect",
    ["Python", "Java", "C++"]
)
gender = st.radio(
    "Gender - radio",
    ["Male", "Female"]
)
agree = st.checkbox("I Agree - checkbox")
if st.button("Submit - button"):
    st.success("Submitted - success")

file = st.file_uploader(
    "Upload File - file_uploader",
    type=["csv", "jpg", "png"]
)

df = pd.DataFrame({
    "Name":["John","Mary"],
    "Age":[22,25]
})

st.write("Table - table")
st.table(df)

st.write("Dataframe - dataframe")
st.dataframe(df)

st.write("JSON - json")
st.json({
    "Name":"John",
    "Age":25
})

data = pd.DataFrame(
    np.random.randn(20,3),
    columns=["A","B","C"]
)

st.write("Line chart - line_chart")
st.line_chart(data)

st.write("Bar chart - bar_chart")
st.bar_chart(data)

st.write("Area Chart - area_chart")
st.area_chart(data)

st.write("Progress bar - progress")

bar = st.progress(0)
for i in range(100):
    time.sleep(0.05)
    bar.progress(i+1)

st.write("Spinner - spinner")
with st.spinner("Loading..."):
    time.sleep(3)

st.success("Success - success")
st.error("Error - error")
st.warning("Warning - warning")
st.info("Information - info")

st.write("Columns - columns")
col1, col2 = st.columns(2)

with col1:
    st.button("Left")

with col2:
    st.button("Right")


st.sidebar.title("Menu - sidebar.title")

option = st.sidebar.selectbox(
    "Choose - sidebar.selectbox",
    ["Home","About"]
)

st.write("Tabs - tabs")
tab1, tab2 = st.tabs(
    ["Home","About"]
)

with tab1:
    st.write("Home Page")

with tab2:
    st.write("About Page")


with st.expander("Show Details - expander"):
    st.write("Hidden content")

with st.form("login - form"):

    username = st.text_input("Username")
    password = st.text_input(
        "Password",
        type="password"
    )

    submit = st.form_submit_button("Login - form_submit_button")

st.write("Container - container")
container = st.container()

with container:
    st.write("Inside Container")

st.write("Placeholder")
placeholder = st.empty()

placeholder.write("Loading...")

placeholder.write("Completed")

st.write("Download button with data 'Hello' and filename = hello.txt - download_button")
st.download_button(
    "Download",
    data="Hello",
    file_name="hello.txt"
)

st.write("Metrics - metric")
st.metric(
    "Revenue",
    "$50,000",
    "+15%"
)

st.write("Session Dictionary - session_state")
if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Increment"):
    st.session_state.count += 1

st.write(st.session_state.count)

st.write("Balloons - snow")
st.balloons()

st.write("Snow - snow")
st.snow()

st.set_page_config(
    page_title="My App",
    page_icon="📊",
    layout="wide"
)
