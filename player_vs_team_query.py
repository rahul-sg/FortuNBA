import pandas as pd
from nba_api.stats.endpoints import playergamelog as nba
from nba_api.stats.endpoints import playerprofilev2
from nba_api.stats.static import players
from nba_api.stats.static import teams

class player_vs_team_query:

    szn_0, szn_1, szn_2 = "2023-24", "2022-23", "2021-22"

    def __init__(self):
        self.nba_players = players.get_active_players()
        pd.options.display.show_dimensions = False

    def get_player_id(self, player_name):
        player_id = [player for player in self.nba_players if player["full_name"] == player_name][0]["id"]
        return player_id
    
    def get_player_team_abv(self, player_name):
        player_team_abv_obj = playerprofilev2.PlayerProfileV2(player_id=self.get_player_id(player_name))
        player_team_abv = player_team_abv_obj.get_data_frames()[0]["TEAM_ABBREVIATION"][len(player_team_abv_obj.get_data_frames()[0]) - 1]
        return player_team_abv
    
    def get_player_game_log(self, player_name, season):
        return nba.PlayerGameLog(player_id=self.get_player_id(player_name), season=season).get_data_frames()[0]

    def query(self, player_name, home_or_away, team_vs):
        test_0 = self.get_player_game_log(player_name, self.szn_0)
        test_1 = self.get_player_game_log(player_name, self.szn_1)
        test_2 = self.get_player_game_log(player_name, self.szn_2)

        search_query = ""
        search_query1 = ""
        search_query2 = ""

        output = []

        if home_or_away.lower() == "home":
            search_query = " vs. " + team_vs
            #print("\nStats of " + player_name + search_query + " for last 3 seasons: \n")
            player_vs_team = test_0[test_0["MATCHUP"].str.contains(search_query)]
            #print(self.szn_0 + ":")
            output += [player_vs_team.iloc[:, 3:-1] if player_vs_team.empty == False else "There were no stats for " + player_name + search_query + \
                                                                        " During the " + self.szn_0 + " season."]
            #print(player_vs_team.iloc[:, 3:-1] if player_vs_team.empty == False else "There were no stats for " + player_name + search_query + \
            #                                                            " During the " + self.szn_0 + " season.")
            #print()
            player_vs_team = test_1[test_1["MATCHUP"].str.contains(search_query)]
            #print(self.szn_1 + ":")
            output += [player_vs_team.iloc[:, 3:-1] if player_vs_team.empty == False else "There were no stats for " + player_name + search_query + \
                                                                        " During the " + self.szn_1 + " season."]
            #print(player_vs_team.iloc[:, 3:-1] if player_vs_team.empty == False else "There were no stats for " + player_name + search_query + \
            #                                                            " During the " + self.szn_1 + " season.")
            #print()
            player_vs_team = test_2[test_2["MATCHUP"].str.contains(search_query)]
            #print(self.szn_2 + ":")
            output += [player_vs_team.iloc[:, 3:-1] if player_vs_team.empty == False else "There were no stats for " + player_name + search_query + \
                                                                        " During the " + self.szn_2 + " season."]
            #print(player_vs_team.iloc[:, 3:-1] if player_vs_team.empty == False else "There were no stats for " + player_name + search_query + \
            #                                                            " During the " + self.szn_2 + " season.")
            #print()

        elif home_or_away.lower() == "away":
            search_query = " @ " + team_vs
            #print("\nStats of " + player_name + search_query + " for last 3 seasons: \n")
            player_at_team = test_0[test_0["MATCHUP"].str.contains(search_query)]
            #print(self.szn_0 + ":")
            output += [player_at_team.iloc[:, 3:-1] if player_at_team.empty == False else "There were no stats for " + player_name + search_query + \
                                                                        " During the " + self.szn_0 + " season."]
            #print(player_at_team.iloc[:, 3:-1] if player_at_team.empty == False else "There were no stats for " + player_name + search_query + \
            #                                                            " During the " + self.szn_0 + " season.")
            #print()
            #print(player_at_team["PTS"].mean())
            player_at_team = test_1[test_1["MATCHUP"].str.contains(search_query)]
            #print(self.szn_1 + ":")
            output += [player_at_team.iloc[:, 3:-1] if player_at_team.empty == False else "There were no stats for " + player_name + search_query + \
                                                                        " During the " + self.szn_1 + " season."]
            #print(player_at_team.iloc[:, 3:-1] if player_at_team.empty == False else "There were no stats for " + player_name + search_query + \
            #                                                            " During the " + self.szn_1 + " season.")
            #print()
            player_at_team = test_2[test_2["MATCHUP"].str.contains(search_query)]
            #print(self.szn_2 + ":")
            output += [player_at_team.iloc[:, 3:-1] if player_at_team.empty == False else "There were no stats for " + player_name + search_query + \
                                                                        " During the " + self.szn_2 + " season."]
            #print(player_at_team.iloc[:, 3:-1] if player_at_team.empty == False else "There were no stats for " + player_name + search_query + \
            #                                                            " During the " + self.szn_2 + " season.")
            #print()
        elif home_or_away.lower() == "both":
            search_query1 = " vs. " + team_vs
            search_query2 = " @ " + team_vs
            #print("\nStats of " + player_name + " against " + team_vs + " for last 3 seasons: \n")
            player_vs_team = test_0[test_0["MATCHUP"].str.contains(search_query1)]
            player_at_team = test_0[test_0["MATCHUP"].str.contains(search_query2)]
            #print(self.szn_0 + ":")
            output += [player_vs_team.iloc[:, 3:-1] if player_vs_team.empty == False else "There were no stats for " + player_name + search_query1 + \
                                                                        " During the " + self.szn_0 + " season.", 
                       player_at_team.iloc[:, 3:-1] if player_at_team.empty == False else "There were no stats for " + player_name + search_query2 + \
                                                                        " During the " + self.szn_0 + " season."]
            #print(player_vs_team.iloc[:, 3:-1] if player_vs_team.empty == False else "There were no stats for " + player_name + search_query1 + \
            #                                                            " During the " + self.szn_0 + " season.")
            #print(player_at_team.iloc[:, 3:-1] if player_at_team.empty == False else "There were no stats for " + player_name + search_query2 + \
            #                                                            " During the " + self.szn_0 + " season.")
            #print()
            player_vs_team = test_1[test_1["MATCHUP"].str.contains(search_query1)]
            player_at_team = test_1[test_1["MATCHUP"].str.contains(search_query2)]
            #print(self.szn_1 + ":")
            output += [player_vs_team.iloc[:, 3:-1] if player_vs_team.empty == False else "There were no stats for " + player_name + search_query1 + \
                                                                        " During the " + self.szn_1 + " season.", 
                       player_at_team.iloc[:, 3:-1] if player_at_team.empty == False else "There were no stats for " + player_name + search_query2 + \
                                                                        " During the " + self.szn_1 + " season."]
            #print(player_vs_team.iloc[:, 3:-1] if player_vs_team.empty == False else "There were no stats for " + player_name + search_query1 + \
            #                                                            " During the " + self.szn_1 + " season.")
            #print(player_at_team.iloc[:, 3:-1] if player_at_team.empty == False else "There were no stats for " + player_name + search_query2 + \
            #                                                            " During the " + self.szn_1 + " season.")
            #print()
            player_vs_team = test_2[test_2["MATCHUP"].str.contains(search_query1)]
            player_at_team = test_2[test_2["MATCHUP"].str.contains(search_query2)]
            #print(self.szn_2 + ":")
            output += [player_vs_team.iloc[:, 3:-1] if player_vs_team.empty == False else "There were no stats for " + player_name + search_query1 + \
                                                                        " During the " + self.szn_2 + " season.", 
                       player_at_team.iloc[:, 3:-1] if player_at_team.empty == False else "There were no stats for " + player_name + search_query2 + \
                                                                        " During the " + self.szn_2 + " season."]
            #print(player_vs_team.iloc[:, 3:-1] if player_vs_team.empty == False else "There were no stats for " + player_name + search_query1 + \
            #                                                            " During the " + self.szn_2 + " season.")
            #print(player_at_team.iloc[:, 3:-1] if player_at_team.empty == False else "There were no stats for " + player_name + search_query2 + \
            #                                                            " During the " + self.szn_2 + " season.")
            #print()
        return output


# def main():
#     query_engine = player_vs_team_query()
    
#     while (True):
#         print("Use [Control + \'C\'] to quit program")
#         player_input = input("Enter player name: ")
#         home_or_away = input("Home or Away or Both: ")
#         team_vs = input("Enter team abbreviation(ABV) to check for matchups: ")
#         print(query_engine.query(player_input, home_or_away, team_vs))

# main()
