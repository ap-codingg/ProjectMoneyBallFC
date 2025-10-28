import pandas as pd
import numpy as np
import ast 

def main():
    #Load cleaned shots data
    shots = pd.read_csv("data/cleaned_shots.csv")
    passes = pd.read_csv("data/cleaned_passes.csv")
    dribbles = pd.read_csv("data/cleaned_dribbles.csv")
    #Shot efficiency per player
    player_shot = shots.groupby('player', as_index=False).agg({
        'shot_statsbomb_xg': 'sum', 'shot_outcome': 'count'
        })
    player_shot['shot_efficiency'] = player_shot['shot_outcome'] - player_shot['shot_statsbomb_xg']
    player_shot = player_shot.reset_index()
    #Pass accuracy per player
    passes['pass_outcome'] = passes['pass_outcome'].astype(str).str.strip().str.lower()
    bad_outcomes = ['incomplete', 'out', 'unknown', 'pass offside', 'injury clearance']
    player_pass = passes.groupby('player', as_index=False).agg(
    successful_passes=('pass_outcome', lambda x: (~x.isin(bad_outcomes)).sum()),
    total_passes=('pass_outcome', 'count'))
    player_pass['pass_accuracy'] = (player_pass['successful_passes'] / player_pass['total_passes'].replace(0, np.nan)) * 100
    #Progressive pass ratio per player
    passes['forward_distance'] = passes['pass_end_location'].apply(lambda x: float(ast.literal_eval(x)[0])) - passes['location'].apply(lambda x: float(ast.literal_eval(x)[0]))
    passes['is_progressive'] = passes['forward_distance'] > 10
    player_progressive = passes.groupby('player', as_index=False).agg(
    forward_distance=('forward_distance', 'sum'),
    total_passes = ('pass_outcome', 'count'),
    progressive_passes = ('is_progressive', 'sum')
    ).reset_index()
    player_progressive['progressive_pass_ratio'] = (player_progressive['progressive_passes'] / player_progressive['total_passes'].replace(0, np.nan)) * 100
    #Dribble success rate per player
    player_dribble = dribbles.groupby('player', as_index=False).agg(
    successful_dribbles = ('dribble_outcome', lambda x: (x == 'Complete').sum()),
    total_dribbles = ('dribble_outcome', 'count'))
    player_dribble['dribble_success_rate'] = (player_dribble['successful_dribbles'] / player_dribble['total_dribbles'].replace(0, np.nan)) * 100
    #Merge all statistics
    player_stats = player_shot[['player', 'shot_efficiency']].merge(
        player_pass[['player', 'pass_accuracy']], on='player', how='outer').merge(
        player_progressive[['player', 'progressive_pass_ratio']], on='player', how='outer').merge(
        player_dribble[['player', 'dribble_success_rate']], on='player', how='outer')
    player_stats = player_stats.fillna(0)
    #Normalize all metrics between 0 and 100 for fair weighting
    for col in ['shot_efficiency', 'pass_accuracy', 'progressive_pass_ratio', 'dribble_success_rate']:
     col_min = player_stats[col].min()
     col_max = player_stats[col].max()
     if col_max > col_min:  #Avoid division by zero
        player_stats[col] = 100 * (player_stats[col] - col_min) / (col_max - col_min)
    #The "Hidden Gem" score: a weighted average of all metrics
    player_stats['hidden_gem_score'] = (
        player_stats['shot_efficiency'] * 0.35 +
        player_stats['pass_accuracy'] * 0.25 +
        player_stats['progressive_pass_ratio'] * 0.10 +
        player_stats['dribble_success_rate'] * 0.30
    )
    #Top 10 Hidden Gems and save to CSV both player stats and hidden gems
    top_hidden_gems = player_stats.sort_values('hidden_gem_score', ascending=False).head(10)
    player_stats.to_csv("data/player_stats.csv", index=False)
    top_hidden_gems.to_csv("data/top_hidden_gems.csv", index=False)
    print("Saved player statistics and top hidden gems.")
    print(top_hidden_gems)
if __name__ == "__main__":
    main()
