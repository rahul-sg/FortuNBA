import pandas as pd
from nba_api.stats.endpoints import playergamelog as nba
from nba_api.stats.endpoints import playerprofilev2
from nba_api.stats.static import players
from nba_api.stats.static import teams

nba_players = players.get_active_players()
pd.options.display.show_dimensions = False

player_input = input("Enter player name: ")
home_or_away = input("Home or Away or Both: ")
team_vs = input("Enter team abbreviation(ABV) to check for matchups: ")
szn_0, szn_1, szn_2 = "2023-24", "2022-23", "2021-22"

player_id = [player for player in nba_players if player["full_name"] == player_input][0]["id"]
player_team_abv_obj = playerprofilev2.PlayerProfileV2(player_id=player_id)
player_team_abv = player_team_abv_obj.get_data_frames()[0]["TEAM_ABBREVIATION"][len(player_team_abv_obj.get_data_frames()[0]) - 1]
test_0 = nba.PlayerGameLog(player_id=player_id, season=szn_0).get_data_frames()[0]
test_1 = nba.PlayerGameLog(player_id=player_id, season=szn_1).get_data_frames()[0]
test_2 = nba.PlayerGameLog(player_id=player_id, season=szn_2).get_data_frames()[0]

search_query = ""
search_query1 = ""
search_query2 = ""

print()

if home_or_away.lower() == "home":
    search_query = " vs. " + team_vs
    player_vs_team = test_0[test_0["MATCHUP"].str.contains(search_query)]
    print(szn_0 + ":")
    print(player_vs_team.iloc[:, 3:-1] if player_vs_team.empty == False else "There were no stats for " + player_input + search_query + \
                                                                " During the " + szn_0 + " season.")
    print()
    player_vs_team = test_1[test_1["MATCHUP"].str.contains(search_query)]
    print(szn_1 + ":")
    print(player_vs_team.iloc[:, 3:-1] if player_vs_team.empty == False else "There were no stats for " + player_input + search_query + \
                                                                " During the " + szn_1 + " season.")
    print()
    player_vs_team = test_2[test_2["MATCHUP"].str.contains(search_query)]
    print(szn_2 + ":")
    print(player_vs_team.iloc[:, 3:-1] if player_vs_team.empty == False else "There were no stats for " + player_input + search_query + \
                                                                " During the " + szn_2 + " season.")
    print()

elif home_or_away.lower() == "away":
    search_query = " @ " + team_vs
    player_at_team = test_0[test_0["MATCHUP"].str.contains(search_query)]
    print(szn_0 + ":")
    print(player_at_team.iloc[:, 3:-1] if player_at_team.empty == False else "There were no stats for " + player_input + search_query + \
                                                                " During the " + szn_0 + " season.")
    print()
    #print(player_at_team["PTS"].mean())
    player_at_team = test_1[test_1["MATCHUP"].str.contains(search_query)]
    print(szn_1 + ":")
    print(player_at_team.iloc[:, 3:-1] if player_at_team.empty == False else "There were no stats for " + player_input + search_query + \
                                                                " During the " + szn_1 + " season.")
    print()
    player_at_team = test_2[test_2["MATCHUP"].str.contains(search_query)]
    print(szn_2 + ":")
    print(player_at_team.iloc[:, 3:-1] if player_at_team.empty == False else "There were no stats for " + player_input + search_query + \
                                                                " During the " + szn_2 + " season.")
    print()
elif home_or_away.lower() == "both":
    search_query1 = " vs. " + team_vs
    search_query2 = " @ " + team_vs
    player_vs_team = test_0[test_0["MATCHUP"].str.contains(search_query1)]
    player_at_team = test_0[test_0["MATCHUP"].str.contains(search_query2)]
    print(szn_0 + ":")
    print(player_vs_team.iloc[:, 3:-1] if player_vs_team.empty == False else "There were no stats for " + player_input + search_query1 + \
                                                                " During the " + szn_0 + " season.")
    print(player_at_team.iloc[:, 3:-1] if player_at_team.empty == False else "There were no stats for " + player_input + search_query2 + \
                                                                " During the " + szn_0 + " season.")
    print()
    player_vs_team = test_1[test_1["MATCHUP"].str.contains(search_query1)]
    player_at_team = test_1[test_1["MATCHUP"].str.contains(search_query2)]
    print(szn_1 + ":")
    print(player_vs_team.iloc[:, 3:-1] if player_vs_team.empty == False else "There were no stats for " + player_input + search_query1 + \
                                                                " During the " + szn_1 + " season.")
    print(player_at_team.iloc[:, 3:-1] if player_at_team.empty == False else "There were no stats for " + player_input + search_query2 + \
                                                                " During the " + szn_1 + " season.")
    print()
    player_vs_team = test_2[test_2["MATCHUP"].str.contains(search_query1)]
    player_at_team = test_2[test_2["MATCHUP"].str.contains(search_query2)]
    print(szn_2 + ":")
    print(player_vs_team.iloc[:, 3:-1] if player_vs_team.empty == False else "There were no stats for " + player_input + search_query1 + \
                                                                " During the " + szn_2 + " season.")
    print(player_at_team.iloc[:, 3:-1] if player_at_team.empty == False else "There were no stats for " + player_input + search_query2 + \
                                                                " During the " + szn_2 + " season.")
    print()
