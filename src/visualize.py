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
    #Heatmap of hidden gems
    stats = ['shot_efficiency', 'pass_accuracy', 'progressive_pass_ratio', 'dribble_success_rate']
    df_sorted = top_hidden_gems.sort_values('hidden_gem_score', ascending = False).head(10)
    plt.figure(figsize = (10, 6))
    sns.heatmap(df_sorted.set_index('player')[stats], annot = True, cmap="YlGnBu", cbar_kws={'label': 'Score'}, fmt=".2f")
    plt.title("Top 10 Hidden Gems")
    plt.xlabel("Stats")
    plt.xticks(rotation = 45)
    plt.ylabel("Player")
    plt.tight_layout()
    plt.savefig("output/hidden_gems_heatmap.png")
    plt.show()
    print("Saved hidden gems heatmap.")

if __name__ == "__main__":
    main()