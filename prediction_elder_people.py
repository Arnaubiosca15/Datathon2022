import pandas as pd
import streamlit as st


st.dataframe(pd.read_json("perfils.json"))