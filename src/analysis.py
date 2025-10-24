import pandas as pd

def main():
    shots = pd.read_csv('data/cleaned_events.csv')
    passes = pd.read_csv('data/cleaned_passes.csv')
    print("Loaded cleaned data")
    #Replace missing xG values with 0
    if 'shot_xG' not in shots.columns:
        print("Column xG per shot not found in data")
        return
    shots['shot_xG'] = shots['shot_xG'].fillna(0)
    #Avg xG per shot
    player_shots = shots.groupby('player', as_index= False).agg({'shot_xG': 'sum', 'shot_outcome': 'count'})
    player_shots['xG_per_shot'] = player_shots['shot_xG'] / player_shots['shot_outcome']
    #Passing accuracy per player
    passes['accurate'] = passes['pass_outcome'].isna()
    player_passes = passes.groupby('player_id', as_index=False).agg({'accurate': 'sum', 'id': 'count'}).rename(columns={'id': 'total_passes'})
    player_passes['passing_accuracy'] = player_passes['accurate'] / player_passes['total_passes']
    #Merge shots and passes
    player_stats = pd.merge(player_shots['player', 'xG_per_shot'], player_passes['player', 'passing_accuracy'], on='player', how='outer')
    summary = summary.fillna(0)
    #Hidden gems
    hidden_gems = summary[(summary['xG_per_shot'] > summary['xG_per_shot'].mean()) & (summary['passing_accuracy'] > summary['passing_accuracy'].mean())]
    hidden_gems = hidden_gems.sort_values(['xG_per_shot', 'passing_accuracy'], ascending=False).head(10)
    hidden_gems.to_csv('data/top_players_by_xG.csv', index=False)
    print("Hidden gems saved to data/top_players_by_xG.csv")
if __name__ == "__main__":
    main()