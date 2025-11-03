# ProjectMoneyBallFC
This project is based on the moneyball method, that consists in analysing different and advanced statistic metrics to take sport decisions, identifying players that have statistics correlated with success but are undervalued by other teams.

Using ['StatsBomb's open data project'](https://github.com/statsbomb/open-data), this project, given a season, identifies the players that are doing better than stand out in:
- Shot efficiency,
- Pass accuracy,
- Progressive pass ratio,
- Dribble success rate.

## Objectives
* Load data from StatsBomb.
* Clean the data, removing unnecessary columns.
* Compute the "hidden gem score", a weighted average of the selected metrics used to identify hidden talents.
* Visualize this hidden talents using an heatmap

## Running the code
The project requires the libraries listed in the requirements.txt.
After installing the dependencies, the scripts to run in order are:
1. load_data.py
2. clean_data.py
3. analysis.py
4. visualize.py
5. app.py

## Author
Project developed by Alberto Polato
