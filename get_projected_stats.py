import pandas as pd
from player_vs_team_query import player_vs_team_query
from player_current_szn_query import player_current_szn_query
from queue import PriorityQueue
from collections import Counter 

class get_projected_stats:

    def __init__(self, player, team_against, home_or_away):
        self.p_v_t_query_engine = player_vs_team_query()
        self.game_log_query_engine = player_current_szn_query()

        self.player = player
        self.team_against = team_against
        self.k = 5
        self.this_season = "2023-24"

        self.query_list = self.p_v_t_query_engine.query(player, home_or_away, team_against)
        self.last_three_szns_df = self.game_log_query_engine.get_player_log_last_three_szns(player)


    def get_prev_matchups_list(self):
        prev_matchups_list = []

        for obj in self.query_list:
            if isinstance(obj, pd.DataFrame):
                prev_matchups_list += [obj]
        
        prev_matchups_df = pd.concat(prev_matchups_list, axis=0).reset_index().iloc[:, 1:-1]
        self.k = pow(len(prev_matchups_df) + 1, 2)

        return prev_matchups_df
        

    def get_average_stat_for_this_season(self, stat):
        this_szn_average = self.game_log_query_engine.get_player_game_log(self.player, self.this_season)[stat].mean()
        return round(this_szn_average, 2)


    def calculate_projected_for_stat(self, stat):
        last_pts = list(self.last_three_szns_df[stat])
        prev_pts = list(self.get_prev_matchups_list()[stat])

        pq = PriorityQueue()

        for i in prev_pts:
            each_game_diffs = []
            for j in last_pts:
                diff = i - j
                each_game_diffs.append(diff)
                pq.put(diff)

        all_diffs = []
        while not pq.empty():
            all_diffs.append(pq.get())

        counter = Counter(all_diffs) 
        most_occur = counter.most_common(self.k)
        #print(most_occur)

        total = 0

        for tup in most_occur:
            total += tup[0]


        projected = self.get_average_stat_for_this_season(stat) + (total / len(most_occur))
        return round(projected, 2)
    
    
    def get_average_for_each_stat(self):
        avg_stats = {}

        for col in self.get_prev_matchups_list():
            if self.get_prev_matchups_list().dtypes[col] == int:
                avg_stats[col] = self.get_average_stat_for_this_season(col)
        
        return avg_stats



    def get_projected_for_each_stat(self):
        proj_stats = {}

        for col in self.get_prev_matchups_list():
            if self.get_prev_matchups_list().dtypes[col] == int:
                proj_stats[col] = self.calculate_projected_for_stat(col)
        
        return proj_stats
    
    def get_avg_vs_proj_report(self):
        avg_stats = self.get_average_for_each_stat()
        proj_stats = self.get_projected_for_each_stat()

        report = pd.DataFrame.from_dict([avg_stats, proj_stats]).transpose().rename(columns={0: 'Average', 1: 'Projected'})

        return report

def main():
    player = "Stephen Curry"

    team_against = "LAL"

    home_or_away = "away"
    stats_proj_engine = get_projected_stats(player, team_against, home_or_away)

    projs = stats_proj_engine.calculate_projected_for_stat("BLK")

    print(projs)

#main()