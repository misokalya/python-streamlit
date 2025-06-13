import streamlit as st

age = st.number_input("Enter your age")

if age < 18:
    st.write("You can not Vote!")
else:
    st.write("You are Allowed to Vote")