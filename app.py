import streamlit as st
# from src.data import load_data, build_monthly
from src.common import mois_fr
import plotly.express as px
import pandas as pd


st.set_page_config(page_title="Patio 2025", layout="wide")
st.sidebar.header("Analyses")




df_grp = df = pd.read_csv("data/patio_2025_monthly.csv", encoding="utf-8")

st.title("Analyse Patio 2025")



