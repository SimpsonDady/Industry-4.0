import copy

from Graph.DataStructure import Data


class Daily:
    def __init__(self, machine_name, execute_format):
        self.machine_name = machine_name
        self.execute_format = execute_format
        self.graph = []
        self.__draw()

    def __draw(self):
        color = ['magenta', 'blue', 'red']
        print(self.machine_name[0])
        for machine in self.execute_format:
            data = Data()
            pre_program = machine[0].program
            end = machine[0].end
            index = data.add_tick(machine[0].knife)
            for j in range(round((machine[0].end - machine[0].start).total_seconds())):
                data.add_line(index, '-', 0.5)
            for i in range(1, len(machine)):
                if machine[i].program != pre_program:
                    start = machine[i-1].start
                    data.add_alltime(start, end, machine[i-1].program)
                    self.graph.append(data)
                    print(len(self.graph[-1].lines),".............")
                    print(self.graph[-1].y_ticks, "y_ticks")
                    print(round((end - machine[i-1].start).total_seconds()))
                    data = Data()
                    end = machine[i].end
                    pre_program = machine[i].program
                    index = data.add_tick(machine[i].knife)
                    for j in range(round((machine[i].end - machine[i].start).total_seconds())):
                        data.add_line(index, '-', 0.5)
                else:
                    for k in range(round((machine[i-1].start - machine[i].end).total_seconds())):
                        data.add_line(0, '-', 0.5)
                    index = data.add_tick(machine[i].knife)
                    for j in range(round((machine[i].end - machine[i].start).total_seconds())):
                        data.add_line(index, '-', 0.5)


