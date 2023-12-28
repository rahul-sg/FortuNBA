import pandas as pd
from player_vs_team_query import player_vs_team_query
from player_current_szn_query import player_current_szn_query
from queue import PriorityQueue
from collections import Counter 
import statistics

query_engine = player_vs_team_query()
game_log = player_current_szn_query()

k = 25
this_season = "2023-24"
team_against = "GSW"

#player_input = input("Enter player name: ")
#home_or_away = input("Home or Away or Both: ")
#team_vs = input("Enter team abbreviation(ABV) to check for matchups: ")
player = "LeBron James"
query_list = query_engine.query(player, "both", team_against)
last_szns_df = game_log.get_player_log_last_three_szns(player)


prev_matchups_list = []

for obj in query_list:
    if isinstance(obj, pd.DataFrame):
        prev_matchups_list += [obj]

prev_matchups_df = pd.concat(prev_matchups_list, axis=0).reset_index().iloc[:, 1:]

#
last_stats = []
prev_matchup_stats = []

for col in last_szns_df:
    last_stats += list(last_szns_df[col])

for col in prev_matchups_df:
    prev_matchup_stats += list(prev_matchups_df[col])
#

last_pts = list(last_szns_df["PTS"])
prev_pts = list(prev_matchups_df["PTS"])

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
most_occur = counter.most_common(k)
#print(most_occur)

total = 0

for tup in most_occur:
    total += tup[0]

#print(total / len(most_occur))

this_szn_average = game_log.get_player_game_log(player, this_season)["PTS"].mean()
projected = this_szn_average + (total / len(most_occur))
#print(this_szn_average
print("Projected Stats vs: " + team_against)
print("Average: " + str(this_szn_average) + "\nProjected: " + str(projected))




# get the player's current season log
# take the average of all the current season game's points
# compare (take difference) it to each previous season matchup game's points
# put each difference into a priority queue
# get the top K differences
