import pandas as pd
from nba_api.stats.endpoints import playergamelog as nba
from nba_api.stats.endpoints import playerprofilev2
from nba_api.stats.static import players
from nba_api.stats.static import teams

class player_current_szn_query:

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
    
    def get_player_log_last_three_szns(self, player_name):
        test_0 = nba.PlayerGameLog(player_id=self.get_player_id(player_name), season=self.szn_0).get_data_frames()[0]
        test_1 = nba.PlayerGameLog(player_id=self.get_player_id(player_name), season=self.szn_1).get_data_frames()[0]
        test_2 = nba.PlayerGameLog(player_id=self.get_player_id(player_name), season=self.szn_2).get_data_frames()[0]

        return pd.concat([test_0, test_1, test_2], axis=0).reset_index().iloc[:, 4:-2]
    
