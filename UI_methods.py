import streamlit as st
import pandas as pd
import numpy as np
import time


st.title("Title - title")
st.markdown("---")

st.header("Header - header")
st.markdown("---")

st.subheader("Sub Header - subheader")
st.markdown("---")

st.text("Plain text")
st.markdown("---")

st.write("Normal text - write")
st.markdown("---")

st.code("print('Hello') - code")
st.markdown("---")

st.latex(r"Formula text E = mc^2 - latex")
st.markdown("---")

name = st.text_input("Enter Name - text_input")
st.markdown("---")

feedback = st.text_area("Feedback - text_area")
st.markdown("---")

age = st.number_input("Age - number_input", 18, 100)
st.markdown("---")

rating = st.slider("Rating - slider", 1, 5, 3)
st.markdown("---")

city = st.selectbox(
    "City - selectbox",
    ["Chennai", "Delhi", "Mumbai"]
)
st.markdown("---")

skills = st.multiselect(
    "Skills - multiselect",
    ["Python", "Java", "C++"]
)
st.markdown("---")

gender = st.radio(
    "Gender - radio",
    ["Male", "Female"]
)
st.markdown("---")

agree = st.checkbox("I Agree - checkbox")
st.markdown("---")

if st.button("Submit - button"):
    st.success("Submitted - success")
st.markdown("---")

file = st.file_uploader(
    "Upload File - file_uploader",
    type=["csv", "jpg", "png"]
)
st.markdown("---")

df = pd.DataFrame({
    "Name":["John","Mary"],
    "Age":[22,25]
})

st.write("Table - table")
st.table(df)
st.markdown("---")

st.write("Dataframe - dataframe")
st.dataframe(df)
st.markdown("---")

st.write("JSON - json")
st.json({
    "Name":"John",
    "Age":25
})
st.markdown("---")

data = pd.DataFrame(
    np.random.randn(20,3),
    columns=["A","B","C"]
)

st.write("Line chart - line_chart")
st.line_chart(data)
st.markdown("---")

st.write("Bar chart - bar_chart")
st.bar_chart(data)
st.markdown("---")

st.write("Area Chart - area_chart")
st.area_chart(data)
st.markdown("---")

st.write("Progress bar - progress")
bar = st.progress(0)
for i in range(100):
    time.sleep(0.05)
    bar.progress(i+1)
st.markdown("---")

st.write("Spinner - spinner")
with st.spinner("Loading..."):
    time.sleep(3)
st.markdown("---")

st.success("Success - success")
st.error("Error - error")
st.warning("Warning - warning")
st.info("Information - info")
st.markdown("---")

st.write("Columns - columns")
col1, col2 = st.columns(2)
with col1:
    st.button("Left")
with col2:
    st.button("Right")
st.markdown("---")

st.sidebar.title("Menu - sidebar.title")
option = st.sidebar.selectbox(
    "Choose - sidebar.selectbox",
    ["Home","About"]
)
st.markdown("---")


st.write("Tabs - tabs")
tab1, tab2 = st.tabs(
    ["Home","About"]
)
with tab1:
    st.write("Home Page")
with tab2:
    st.write("About Page")
st.markdown("---")

with st.expander("Show Details - expander"):
    st.write("Hidden content")
st.markdown("---")

st.write("Form - form")
with st.form("login"):
    username = st.text_input("Username")
    password = st.text_input(
        "Password",
        type="password"
    )
    submit = st.form_submit_button("Login - form_submit_button")
st.markdown("---")

st.write("Container - container")
container = st.container()
with container:
    st.write("Inside Container")
st.markdown("---")

st.write("Placeholder")
placeholder = st.empty()
placeholder.write("Loading...")
placeholder.write("Completed")
st.markdown("---")

st.write("Download button with data 'Hello' and filename = hello.txt - download_button")
st.download_button(
    "Download",
    data="Hello",
    file_name="hello.txt"
)
st.markdown("---")

st.write("Metrics - metric")
st.metric(
    "Revenue",
    "$50,000",
    "+15%"
)
st.markdown("---")

st.write("Session Dictionary - session_state")
if "count" not in st.session_state:
    st.session_state.count = 0
if st.button("Increment"):
    st.session_state.count += 1
st.write(st.session_state.count)
st.markdown("---")

st.write("Balloons - snow")
st.balloons()
st.markdown("---")

st.write("Snow - snow")
st.snow()
st.markdown("---")

st.write("Page - set_page_config")
st.set_page_config(
    page_title="My App",
    page_icon="📊",
    layout="wide"
)
