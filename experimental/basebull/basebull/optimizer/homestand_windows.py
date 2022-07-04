"""Sort teams by number of homestands."""
# pylint: disable=E1136

import plotly.graph_objects as go

from basebull.model.schedule import ranges_with_gap, Schedule, TEAM_LIST
from basebull.model.ballparks import team_color


def get_team_homestand_map(schedule_data, gap=1):
    """Returns team_homestead map."""
    team_window_map = {}
    for team in TEAM_LIST:
        team_window_map[team] = ranges_with_gap(schedule_data.park_window(team), gap)

    team_homestand_list = sorted(team_window_map.items(), key=lambda x: x[1])
    return team_homestand_list


def visualize(schedule_data, teams):
    """Line chart of all teams home schedules."""
    gameday_number = list(range(1, 186))
    fig = go.Figure()
    for i, team in enumerate(teams):
        team_dates = [game.date for game in schedule_data.team_schedule(team)]
        if team == "Yankees":
            print(team_dates)
        value = [i * -1 + 30 if j in team_dates else None for j in gameday_number]
        fig.add_trace(
            go.Scatter(
                x=gameday_number, y=value, name=team, mode="markers", marker=dict(size=10, color=team_color(team))
            )
        )
    fig.show()


def debug():
    """Debugger used to build module."""
    schedule_data = Schedule()
    team_homestand_list = get_team_homestand_map(schedule_data)
    team_homestand_list.sort()
    for team_homestand in team_homestand_list:
        print(team_homestand[0], ":", team_homestand[1])

    TEAM_LIST.sort()
    visualize(schedule_data, TEAM_LIST)


if __name__ == "__main__":
    debug()
