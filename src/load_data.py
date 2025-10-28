from statsbombpy import sb
import pandas as pd

def main():
    #Download matches data for Men's World Cup 2022
    print("Downloading matches data...")
    matches = sb.matches(competition_id=43, season_id=106)

    if matches.empty:
        print("No matches found. Check competition_id/season_id.")
        return

    all_events = []

    #Download the events of the first 15 matches
    for match_id in matches.match_id.head(15):
        print(f"Loading events for match {match_id}...")
        events = sb.events(match_id=match_id)
        all_events.append(events)

    events = pd.concat(all_events, ignore_index = True)
    events.to_csv("data/events.csv", index = False)
    print("Saved data.")

if __name__ == "__main__":
    main()