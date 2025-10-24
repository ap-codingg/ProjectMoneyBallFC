import pandas as pd

def main():
    events = pd.read_csv('data/events.csv')
    print("Loaded events data")
    #Basic cleaning: remove rows with missing values
    events_cleaned = events.dropna(subset=['event_type', 'player_id', 'team_id'])  
    #Keep only rows with type == 'shot', 'passes', 'dribble'
    shots= events_cleaned[events_cleaned['event_type'] == 'shot'].copy()
    passes = events_cleaned[events_cleaned['event_type'] == 'pass'].copy()

    #Save cleaned data
    shots.to_csv('data/cleaned_shots.csv', index=False)
    passes.to_csv('data/cleaned_passes.csv', index=False)
    print("Cleaned data saved to data/cleaned_shots.csv, data/cleaned_passes.csv, data/cleaned_dribbles.csv")

if __name__ == "__main__":
    main()