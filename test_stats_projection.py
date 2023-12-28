from get_projected_stats import get_projected_stats

def main():
    player = input("Enter Player: ")
    player1 = "LeBron James"

    team_against = input("Enter Matchup Abbreviation: ")
    team_against1 = "GSW"

    home_or_away = input("Home or Away: ")
    home_or_away1 = "home"
    stats_proj_engine = get_projected_stats(player, team_against, home_or_away)

    projs = stats_proj_engine.get_avg_vs_proj_report()

    print(projs)

main()