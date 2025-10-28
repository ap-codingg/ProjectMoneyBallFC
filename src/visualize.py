import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    player_stats = pd.read_csv("data/player_stats.csv")
    top_hidden_gems = pd.read_csv("data/top_hidden_gems.csv")
    #Check if data is loaded correctly
    if player_stats.empty or top_hidden_gems.empty:
        print("Player statistics or top hidden gems data is missing. Run analysis.py first.")
        return
    