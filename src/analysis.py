import pandas as pd
import numpy as np

def main():
    #Load cleaned shots data
    shots = pd.read_csv("data/cleaned_shots.csv")
    passes = pd.read_csv("data/cleaned_passes.csv")
    dribbles = pd.read_csv("data/cleaned_dribbles.csv")
    #Shot efficiency per player
    player_shot = shots.groupby('player', as_index=False).agg({
        'shot_statsbomb_xg': 'sum', 'shot_outcome': 'count'})
    player_shot['shot_efficiency'] = player_shot['shot_outcome'] - player_shot['shot_statsbomb_xg']
    #Pass accuracy per player
    player_pass = passes.groupby('player', as_index=False).agg({
        'pass_outcome': lambda x: (x == 'Successful').sum(), 'player': 'count'})
    player_pass.rename(columns= {'player': 'total_passes'}, inplace=True)
    player_pass['pass_accuracy'] = (player_pass['pass_outcome'] / player_pass['total_passes'].replace(0, np.nan)) * 100
    #Progressive pass ratio per player
    passes['forward_distance'] = passes['pass_end_location'].apply(lambda x: x[0]) - passes['location'].apply(lambda x: x[0])
    passes['is_progressive'] = passes['forward_distance'] > 10
    player_progressive = passes.groupby('player', as_index=False).agg(
        total_passes = (is_progressive:= 'count'),
        progressive_passes = (is_progressive:= 'sum')
    ).reset_index()
    player_progressive['progressive_pass_ratio'] = (player_progressive['progressive_passes'] / player_progressive['total_passes'].replace(0, np.nan)) * 100
    #Dribble success rate per player
    player_dribble = dribbles.groupby('player', as_index=False).agg({
        'dribble_outcome': lambda x: (x == 'Successful').sum(), 'player': 'count'})
    player_dribble.rename(columns= {'player': 'total_dribbles'}, inplace=True)
    player_dribble['dribble_success_rate'] = (player_dribble['dribble_outcome'] / player_dribble['total_dribbles'].replace(0, np.nan)) * 100
    #Merge all statistics
    player_stats = player_shot[['player', 'shot_efficiency']].merge(
        player_pass[['player', 'pass_accuracy']], on='player', how='outer').merge(
        player_progressive[['player', 'progressive_pass_ratio']], on='player', how='outer').merge(
        player_dribble[['player', 'dribble_success_rate']], on='player', how='outer')
    player_stats = player_stats.fillna(0)
