import streamlit as st

number = st.number_input("Enter any number")

if number%2 == 0:
    st.write("The number is Even")
else:
    st.write("The number is Odd")