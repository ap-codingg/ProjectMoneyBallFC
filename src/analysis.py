import pandas as pd
import numpy as np

def main():
    #Load cleaned shots data
    shots = pd.read_csv("data/cleaned_shots.csv")
    passes = pd.read_csv("data/cleaned_passes.csv")
    dribbles = pd.read_csv("data/cleaned_dribbles.csv")
    #Shot efficiency
    player_shot = shots.groupby('player', as_index=False).agg({
        'shot_statsbomb_xg': 'sum', 'shot_outcome': 'count'})
    player_shot['shot_efficiency'] = player_shot['shot_outcome'] - player_shot['shot_statsbomb_xg']
    #Pass accuracy
    player_pass = passes.groupby('player', as_index=False).agg({
        'pass_outcome': lambda x: (x == 'Successful').sum(), 'player': 'count'})
    player_pass.rename(columns={'player': 'total_passes'}, inplace=True)
    player_pass['pass_accuracy'] = player_pass['pass_outcome'] / player_pass['total_passes'].replace(0, np.nan)
    