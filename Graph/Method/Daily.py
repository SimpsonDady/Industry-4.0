from Graph.Method.Data import Data


class Daily:
    def __init__(self, dmg, machine_name):
        self.dmg = dmg
        self.graph = []
        self.__machine_depend(True)
        self.__machine_depend(False)

    def __machine_depend(self, independent):
        for machine in self.dmg:
            # execute major
            for day in range(len(machine.execute_spend)):
                search = -1
                if independent:
                    self.graph.append(Data(machine.machine_name + '_' + machine.execute_spend[day].getDay()))
                else:
                    for i in range(len(self.graph)):
                        if machine.execute_spend[day].getDay() == self.graph[i].getday():
                            search = i
                    if search == -1:
                            self.graph.append(Data(machine.execute_spend[day].getDay()))

                # ****status section****
                if independent:
                    perday = []                 # To save one line in a day
                    for i in range(0, 86400):   # 1 day = 86400 seconds
                        perday.append(0)
                    self.graph[search].add_tick('Run')
                    # if read 1, than let perday in range of start to end become 1
                    for j in range(machine.status_spend[day].getProgramLength()):
                        if machine.status_spend[day].getProgramCode(j) == 1:
                            for k in range(int(machine.status_spend[day].getStartSecond(j)),
                                           int(machine.status_spend[day].getEndSecond(j))):
                                perday[k] = 1
                    self.graph[search].add_line(perday, 'r', 0.5)
                # ****execute section****
                execute_list = {}    # let every execute code have a number
                perday = []          # initialize perday
                for i in range(0, 86400):
                    perday.append(0)
                # find out all of execute codes, and mark them within execute_num
                for j in range(machine.execute_spend[day].getProgramLength()):
                    code = machine.execute_spend[day].getProgramCode(j)
                    if code not in execute_list and code != 'TOOL-SL-D.I' and code != 'WARM':
                        execute_list.update({machine.execute_spend[day].getProgramCode(j): self.graph[search].gethight()})
                        self.graph[search].add_tick(machine.execute_spend[day].getProgramCode(j))  # set label with execute code to y-axis
                # use execute_list to edit perday
                for j in range(machine.execute_spend[day].getProgramLength()):
                    if machine.execute_spend[day].getProgramCode(j) in execute_list:
                        for k in range(int(machine.execute_spend[day].getStartSecond(j)+0.5),
                                       int(machine.execute_spend[day].getEndSecond(j)+0.5)):
                            perday[k] = execute_list[machine.execute_spend[day].getProgramCode(j)]
                self.graph[search].add_line(perday, 'b', 1)
                # ****plan section****
                if independent:
                    self.graph[search].add_tick('')
                    plan_list = {}
                    perday = []                 # initialize perday
                    for i in range(0, 86400):
                        perday.append(0)
                    for k in range(len(machine.plan_spend)):
                        # find the day execute is handling, or do nothing in this day
                        if machine.execute_spend[day].getDay() == machine.plan_spend[k].getDay():
                            # find out all of execute codes, and mark them within plan_num
                            for j in range(machine.plan_spend[k].getProgramLength()):
                                if machine.plan_spend[k].getProgramCode(j) not in plan_list:
                                    plan_list.update({machine.plan_spend[k].getProgramCode(j): self.graph[search].gethight()})
                                    self.graph[search].add_tick(machine.plan_spend[k].getProgramCode(j))
                            # use plan_list to edit perday
                            for j in range(machine.plan_spend[k].getProgramLength()):
                                for l in range(int(machine.plan_spend[k].getStartSecond(j) + 0.5),
                                               int(machine.plan_spend[k].getEndSecond(j) + 0.5)):
                                    perday[l] = plan_list[machine.plan_spend[k].getProgramCode(j)]
                    self.graph[search].add_line(perday, 'g', 1)
                self.graph[search].add_tick('')
