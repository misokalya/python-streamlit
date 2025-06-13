import streamlit as st

length = st.number_input("Enter Length")
width = st.number_input("Enter Width")

area = length*width

st.write(area)
