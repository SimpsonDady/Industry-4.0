from Graph.Daily import Daily
from Graph.Draw import Draw


class Graph:
    def __init__(self, machine_name, match, status_format, execute_format, plan_format):
        print('****Graph format into image****')
        print(' ->Graphing...')
        daily = Daily(machine_name, match, status_format, execute_format, plan_format)
        print(' ->Saving...')
        graph = Draw(daily.graph)
        print()
