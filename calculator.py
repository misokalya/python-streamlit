import streamlit as st

x = st.number_input("Enter first number")
y = st.number_input("Enter second number")

add = st.write(x+y)
subtract = st.write(x-y)
multiply = st.write(x*y)
divide = st.write(x/y)

