import pandas as pd

def main():
    events = pd.read_csv("data/events.csv")

    #Only keep relevant events: passes, shots, and dribbles
    shots = events[events['type'] == 'Shot'].copy()
    passes = events[events['type'] == 'Pass'].copy()
    dribbles = events[events['type'] == 'Dribble'].copy()
    #Delete unnecessary columns
    shots = shots[['player_name', 'minute', 'second', 'team_name', 'location', 'shot_outcome','shot_statsbomb_xg', 'shot_end_location']]
    passes = passes[['player_name', 'minute', 'second', 'team_name', 'location', 'pass_outcome', 'pass_end_location']]
    dribbles = dribbles[['player_name', 'minute', 'second', 'team_name', 'location', 'dribble_outcome']]
    #Save cleaned data
    shots.to_csv("data/cleaned_shots.csv", index=False)
    passes.to_csv("data/cleaned_passes.csv", index=False)
    dribbles.to_csv("data/cleaned_dribbles.csv", index=False)

    print("Saved cleaned data for shots, passes, and dribbles.")