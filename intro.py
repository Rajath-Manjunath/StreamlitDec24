import streamlit as st
st.title("Learning Streamlit")
st.header("My first app")
st.write("Learning streamlit for the first time")
agree=st.checkbox("Rajath is a great husband")
if agree:
    st.write("Congrats on marrying him GUND")