import pandas as pd

def main():
    #Load cleaned shots data
    shots = pd.read_csv("data/cleaned_shots.csv")
    passes = pd.read_csv("data/cleaned_passes.csv")
    dribbles = pd.read_csv("data/cleaned_dribbles.csv")
    #Shot efficiency
    player_shot = shots.groupby('player', as_index=False).agg({
        'shot_statsbomb_xg': 'sum', 'shot_outcome': 'count'})
    player_shot['shot_efficiency'] = player_shot['shot_statsbomb_xg'] / player_shot['shot_outcome']
    