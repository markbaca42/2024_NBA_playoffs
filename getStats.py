from nba_api.stats.endpoints import playercareerstats
from nba_api.live.nba.endpoints import scoreboard
from nba_api.stats.static.teams import *
from nba_api.stats.static.players import *

from nba_api.stats.endpoints import *
import pandas as pd
import csv


# TEAM IDs
MAVS_ID = 1610612742
CELTICS_ID = 1610612738
HORNETS_ID = 1610612766

# IMPORTANT PLAYER IDs
GAFFORD_ID = 1629655
WASHINGTON_ID = 1629023
LUKA_ID = 1629029
KYRIE_ID = 202681
WILLIAMS_ID = 1629684
LIVELY_ID = 1641726
POWELL_ID = 203939
JONESJR_ID = 1627884
KLEBER_ID = 1628467
GREEN_ID = 1630182
THJ_ID = 203501

MAVS_PLAYERS = [GAFFORD_ID, WASHINGTON_ID, LUKA_ID, KYRIE_ID, LIVELY_ID, POWELL_ID, JONESJR_ID, KLEBER_ID, GREEN_ID, THJ_ID]



# create playersStats.csv
for player_id in MAVS_PLAYERS:
    stats = playergamelog.PlayerGameLog(player_id=str(player_id),season_type_all_star="Playoffs" )
    df = stats.get_data_frames()
    df[0].to_csv('playerStats.csv', mode='a')

# create gameStats.csv
team_stats = teamgamelog.TeamGameLog(team_id=str(MAVS_ID), season_type_all_star="Playoffs")
team_df = team_stats.get_data_frames()
team_df[0].to_csv('teamStats.csv')


