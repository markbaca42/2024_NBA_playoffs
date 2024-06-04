from nba_api.stats.endpoints import playercareerstats
from nba_api.live.nba.endpoints import scoreboard
from nba_api.stats.static.teams import *
from nba_api.stats.static.players import *
from nba_api.stats.endpoints import *

from nba_api.stats.endpoints import *
import pandas as pd
import csv


# TEAM IDs
MAVS_ID = 1610612742
CELTICS_ID = 1610612738
THUNDER_ID = 1610612760
NUGGETS = 1610612743
KNICKS_ID = 1610612752
TWOLVES_ID = 1610612750
# BUCKS_ID = 
# CLIPPERS_ID = 
# CAVS_ID = 
# MAGIC_ID =
# SUNS_ID = 




def getPlayoffs():
    #stats = boxscorehustlev2.BoxScoreHustleV2()
    team_stats = teamgamelog.TeamGameLog(team_id=str(MAVS_ID), season="2021",season_type_all_star="Playoffs")
    team_df = team_stats.get_data_frames()
    team_df[0].to_csv('bigStats/teamStats.csv')

    for year in range(2019, 2024):
        playoffs = leaguegamelog.LeagueGameLog(season=str(year), season_type_all_star="Playoffs")
        playoffs_df = playoffs.get_data_frames()
        playoffs_df[0].to_csv('bigStats/playoffs.csv', mode='a')
        print(len(playoffs_df))

def getTeamHustleStats():
    team_hustle_stats = boxscorehustlev2.BoxScoreHustleV2(game_id=42300225)

def main():
    getTeamHustleStats()
    print("heello world")


if __name__ == "__main__":
    main()