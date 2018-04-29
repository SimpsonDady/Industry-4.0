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
        for execute_format in self.execute_format:
            for machine in execute_format:
                knifeList = []
                data = Data()
                print(machine.program)
                for i in machine.knife:
                    data.sort_y_tick(i.knife)
                for i in range(len(machine.knife)):
                    print(machine.knife[i].knife)
                    print(machine.knife[i].start)
                    print(machine.knife[i].end)
                    index = data.add_tick(machine.knife[i].knife)
                    for k in range(round((machine.knife[i - 1].start - machine.knife[i].end).total_seconds())):
                        data.add_line(0, '-', 0.5)
                    for j in range(round((machine.knife[i].end - machine.knife[i].start).total_seconds())):
                        data.add_line(index, '-', 0.5)
                    data.add_alltime(machine.knife[i].start, machine.knife[i].end, machine.program)
                self.graph.append(data)

        #
        #             for sort in range(i, len(machine)):
        #                 if machine[sort].program != pre_program:
        #                     break
        #                 data.sort_y_tick(machine[sort].knife)
        #             index = data.add_tick(machine[i].knife)
        #             for j in range(round((machine[i].end - machine[i].start).total_seconds())):
        #                 data.add_line(index, '-', 0.5)
        #
        # for machine in self.execute_format:
        #     data = Data()
        #     pre_program = machine[0].program
        #     end = machine[0].end
        #     for sort in range(0,len(machine)):
        #         if machine[sort].program != pre_program:
        #             break
        #         data.sort_y_tick(machine[sort].knife)
        #     index = data.add_tick(machine[0].knife)
        #     for j in range(round((machine[0].end - machine[0].start).total_seconds())):
        #         data.add_line(index, '-', 0.5)
        #     for i in range(1, len(machine)):
        #         if machine[i].program != pre_program:
        #             start = machine[i-1].start
        #             data.add_alltime(start, end, machine[i-1].program)
        #             self.graph.append(data)
        #             print(len(self.graph[-1].lines),".............")
        #             print(self.graph[-1].y_ticks, "y_ticks")
        #             print(round((end - machine[i-1].start).total_seconds()))
        #             data = Data()
        #             end = machine[i].end
        #             pre_program = machine[i].program
        #             for sort in range(i, len(machine)):
        #                 if machine[sort].program != pre_program:
        #                     break
        #                 data.sort_y_tick(machine[sort].knife)
        #             index = data.add_tick(machine[i].knife)
        #             for j in range(round((machine[i].end - machine[i].start).total_seconds())):
        #                 data.add_line(index, '-', 0.5)
        #         else:
        #             for k in range(round((machine[i-1].start - machine[i].end).total_seconds())):
        #                 data.add_line(0, '-', 0.5)
        #             index = data.add_tick(machine[i].knife)
        #             for j in range(round((machine[i].end - machine[i].start).total_seconds())):
        #                 data.add_line(index, '-', 0.5)


