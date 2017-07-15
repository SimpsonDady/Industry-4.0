from Graph.Method.Daily import Daily
from Graph.Method.Graph import Graph


class CreateGraph:
    def __init__(self, dmg):
        daily = Daily(dmg)
        graph = Graph(daily.graph)
