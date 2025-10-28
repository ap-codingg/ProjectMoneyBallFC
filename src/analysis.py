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
    player_pass.rename(columns={'player': 'total_passes'}, inplace=True)
    player_pass['pass_accuracy'] = (player_pass['pass_outcome'] / player_pass['total_passes'].replace(0, np.nan)) * 100
    #Progressive pass ratio per player
    passes['forward_distance'] = passes['pass_end_location'].apply(lambda x: x[0]) - passes['location'].apply(lambda x: x[0])
    passes['is_progressive'] = passes['forward_distance'] > 10
    player_progressive = passes.groupby('player', as_index=False).agg(
        total_passes = (is_progressive := 'count'),
        progressive_passes = (is_progressive := 'sum')
    ).reset_index()
    player_progressive['progressive_pass_ratio'] = (player_progressive['progressive_passes'] / player_progressive['total_passes'].replace(0, np.nan)) * 100
