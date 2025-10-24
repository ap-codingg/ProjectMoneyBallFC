import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("MoneyballFC")

data = pd.read_csv('data/top_players_by_xG.csv')
st.subheader("Top 10 Hidden Gems")
st.dataframe(data)

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='avg_xG', y='player', data=data, ax=ax)
st.pyplot(fig)