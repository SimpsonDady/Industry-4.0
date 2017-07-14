from Graph.Method.Daily import Daily
from Graph.Method.Graph import Graph


class CreateGraph:
    def __init__(self, dmg):
        machine_name = []
        for machine in dmg:
            machine_name.append(machine.machine_name)
        daily = Daily(dmg, machine_name)
        graph = Graph(daily.graph)
