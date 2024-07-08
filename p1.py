import streamlit as st
import pandas as pd
# st.title("my name is uday")
# st.header("this is my website")
# st.subheader("welcome to my website")

name = st.text_input("Enter your name : ")
fname = st.text_input("Enter your father name : ")
adr = st.text_area("Enter your address : ")
classdata = st.selectbox("Enter your class :", (1,2,3,4,5,6))


button = st.button("done")
if button:
    st.markdown(f"""
    Name ={name}
    Father Name = {fname}
    Address = {adr}
    Class= {classdata}
         """)