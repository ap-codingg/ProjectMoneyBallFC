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

## Guide to install the project
* First of all, to clone the repository, use the command:
git clone https://github.com/ap-codingg/ProjectMoneyBallFC
cd ProjectMoneyBallFC
* Then it's better to create a virtual environment, so that the dependencies are installed just to make the code run and will stay on your computer just until the venv is available. To create it, use:
python -m venv .venv
source .venv\Scripts\activate
* Now it's time to install the dependencies contained in the requirements:
pip install -r requirements.txt 

## Running the code
After installing the dependencies, the scripts to run in order are:
1. load_data.py
2. clean_data.py
3. analysis.py
4. visualize.py
5. app.py

## Author
Project developed by Alberto Polato
