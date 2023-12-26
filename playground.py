import pandas as pd
from nba_api.stats.endpoints import playergamelog as nba
from nba_api.stats.static import players
from nba_api.stats.endpoints import playerprofilev2

nba_players = players.get_active_players()

player_input = input("Enter Player name: ")
home_or_away = input("Home or Away or Both: ")
team_vs = input("Enter team ABV to check for matchups: ")
home_search = ""

player_id = [player for player in nba_players if player["full_name"] == player_input][0]["id"]
player_team_abv_obj = playerprofilev2.PlayerProfileV2(player_id=player_id)
player_team_abv = player_team_abv_obj.get_data_frames()[0]["TEAM_ABBREVIATION"][0]
test_0 = nba.PlayerGameLog(player_id=player_id, season="2023-24").get_data_frames()[0]
test_1 = nba.PlayerGameLog(player_id=player_id, season="2022-23").get_data_frames()[0]
test_2 = nba.PlayerGameLog(player_id=player_id, season="2021-22").get_data_frames()[0]
#print(player_team_abv)

search_query = ""
search_query1 = ""
search_query2 = ""

if home_or_away == "Home":
    search_query = player_team_abv + " vs. " + team_vs
    player_vs_team = test_0[test_0["MATCHUP"] == search_query]
    print(player_vs_team)
    player_vs_team = test_1[test_1["MATCHUP"] == search_query]
    print(player_vs_team)
    player_vs_team = test_2[test_2["MATCHUP"] == search_query]
    print(player_vs_team)

elif home_or_away == "Away":
    search_query = player_team_abv + " @ " + team_vs
    player_at_team = test_0[test_0["MATCHUP"] == search_query]
    print(player_at_team)
    player_at_team = test_1[test_1["MATCHUP"] == search_query]
    print(player_at_team)
    player_at_team = test_2[test_2["MATCHUP"] == search_query]
    print(player_at_team)
else:
    search_query1 = player_team_abv + " vs. " + team_vs
    search_query2 = player_team_abv + " @ " + team_vs
    player_vs_team = test_0[test_0["MATCHUP"] == search_query1]
    player_at_team = test_0[test_0["MATCHUP"] == search_query2]
    print(player_vs_team)
    print(player_at_team)
    player_vs_team = test_1[test_1["MATCHUP"] == search_query1]
    player_at_team = test_1[test_1["MATCHUP"] == search_query2]
    print(player_vs_team)
    print(player_at_team)
    player_vs_team = test_2[test_2["MATCHUP"] == search_query1]
    player_at_team = test_2[test_2["MATCHUP"] == search_query2]
    print(player_vs_team)
    print(player_at_team)
