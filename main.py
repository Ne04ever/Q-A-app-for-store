import streamlit as st
from helper_qa import make_few_shot_db_chain

st.title("AtliQ T Shirts: Database Q&A 👕")

question = st.text_input("Question: ")

if question:
    chain = make_few_shot_db_chain()
    response = chain.run(question)

    st.header("Answer")
    st.write(response)