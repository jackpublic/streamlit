import streamlit as st
import pandas as pd
 
st.write("""
# My first app
Hello *world!*
""")

st.markdown("Use some for [RAG](https://gradient.com)")

df = pd.read_csv("AAPL.csv")
st.line_chart(df)

