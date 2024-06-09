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

champs_dict = {1985:'Lakers', 1986: 'Celtics', 1987: 'Lakers', 1988: 'Lakers',1989: 'Pistons',
                1990: 'Pistons', 1991: 'Bulls', 1992: 'Bulls', 1993: 'Bulls', 1994: 'Rockets', 1996: 'Bulls', 1997: 'Bulls', 1998: 'Bulls', 1999: 'Spurs', 
                2000: 'Lakers', 2001: 'Lakers', 2002: 'Lakers', 2003: 'Spurs', 2004: 'Pistons', 2005: 'Spurs', 2006: 'Heat', 2007: 'Spurs', 2008: 'Celtics', 2009: 'Lakers', 
                2010: 'Lakers', 2011: 'Mavericks', 2012: 'Heat', 2013: 'Heat', 2014: 'Spurs', 2015: 'Warriors', 2016: 'Cavaliers', 2017: 'Warriors', 2018: 'Warriors', 2019: 'Raptors', 
                2020: 'Lakers', 2021: 'Bucks', 2022: 'Warriors', 2023: 'Nuggets'}



def getChampions():
    team_stats = teaminfocommon.TeamInfoCommon(team_id=MAVS_ID)
    team_df = team_stats.get_data_frames()
    team_df[0].to_csv('bigStats/champions.csv')


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

def getChampStats():
    # get the team IDs
    standings = leaguestandingsv3.LeagueStandingsV3()
    standings_df = standings.get_data_frames()
    standings_df[0].to_csv('bigStats/standings.csv')
    standings_df = standings_df[0]

    # load the values into a dict
    team_id_dict = {}
    for index, row in standings_df.iterrows():
        team_name = str(row['TeamName'])
        team_id_dict[team_name]= int(row['TeamID'])

    total_cols = ['Team_ID','FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'YEAR', 'TEAM']
    cols_to_keep = ['Team_ID','FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
    total_df = pd.DataFrame(columns=total_cols)

    for year, champ in champs_dict.items():
        team_id = team_id_dict[champ]
        print(str(year) + champ + str(team_id))
        champ_year_data = teamgamelog.TeamGameLog(team_id= team_id, season=str(year-1))
        champ_year_df = champ_year_data.get_data_frames()
        champ_year_df = champ_year_df[0]

        filtered_champ_year_df = champ_year_df[cols_to_keep]

        average_row = filtered_champ_year_df.mean(numeric_only=True)
        average_row_df = average_row.to_frame().T
        average_row_df['YEAR'] = year
        average_row_df['TEAM'] = champ
        print(average_row_df)
        total_df = pd.concat([total_df, average_row_df], ignore_index=True)

    # write total_df to csv
    columns_order = ['TEAM', 'YEAR'] + [col for col in total_df.columns if col not in ['TEAM', 'YEAR']]
    total_df = total_df[columns_order]
    total_df.to_csv('bigStats/total_data.csv', index=False)

def getTeamIDs():
    pass

def getTeamHustleStats():
    team_hustle_stats = boxscorehustlev2.BoxScoreHustleV2(game_id=42300225)

def main():
    getChampStats()
    print("heello world")


if __name__ == "__main__":
    main()