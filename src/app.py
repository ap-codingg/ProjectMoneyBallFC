import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Hidden Gems Finder")

data = pd.read_csv("data/top_hidden_gems.csv")
if data.empty:
    st.error("No data available. Please run the analysis script first.")
else:
    st.subheader("Who is the top player?")
    data.index = data.index + 1
    st.dataframe(data)
    #Heatmap interactive visualization
    stats = ['shot_efficiency', 'pass_accuracy', 'progressive_pass_ratio', 'dribble_success_rate']
    plt.figure(figsize = (10, 6))
    sns.heatmap(data.set_index('player')[stats], annot = True, cmap = "YlGnBu", cbar_kws = {'label': 'Score'}, fmt = ".2f")
    plt.title("Top Hidden Gems")
    plt.xlabel("Stats")
    plt.xticks(rotation = 45)
    plt.ylabel("Player")
    plt.tight_layout()
    st.pyplot(plt)
    st.success("Visualization complete.")

