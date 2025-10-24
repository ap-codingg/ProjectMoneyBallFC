import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    data = pd.read_csv('data/top_players_by_xG.csv')
    if data.empty:
        print("No data available to visualize. Run analysis.py first.")
        return
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x='avg_xG', y='player', data=data)
    plt.title('Top 10 Hidden Gems')
    plt.xlabel('Passing accuracy')
    plt.ylabel('xG per shot')
    plt.tight_layout()
    plt.savefig('data/top_players_by_xG.png')
    print("Visualization saved as top_players_by_xG.png")

if __name__ == "__main__":
    main()
