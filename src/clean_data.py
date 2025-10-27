import pandas as pd

def main():
    events = pd.read_csv("data/events.csv")

    #Only keep relevant events: passes, shots, and dribbles
    shots = events[events['type'] == 'Shot'].copy()
    passes = events[events['type'] == 'Pass'].copy()
    dribbles = events[events['type'] == 'Dribble'].copy()