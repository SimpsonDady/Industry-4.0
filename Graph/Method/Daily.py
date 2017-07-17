from Graph.Method.Data import Data


class Daily:
    def __init__(self, dmg):
        self.dmg = dmg
        self.graph = []
        self.__draw(True)
        self.__draw(False)

    def __draw(self, independent):
        color = ['black', 'green', 'blue']
        for machine in self.dmg:
            if independent:
                machine_name = machine.machine_name + '_'
                label_name = ''
            else:
                machine_name = ''
                label_name = machine.machine_name + '_'
            # execute major
            for day in range(len(machine.execute_spend)):
                search = -1
                for i in range(len(self.graph)):
                    if machine.execute_spend[day].getDay() == self.graph[i].getday():
                        search = i
                if search == -1:
                    self.graph.append(Data(machine_name + machine.execute_spend[day].getDay()))
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
                    self.graph[search].add_line(perday, 'red', '-', 0.5, 'Status')
                # ****execute section****
                list = {}    # let every execute code have a number
                perday = []          # initialize perday
                for i in range(0, 86400):
                    perday.append(0)
                # find out all of execute codes, and mark them within execute_num
                for j in range(machine.execute_spend[day].getProgramLength()):
                    code = machine.execute_spend[day].getProgramCode(j)
                    if code not in list and code != 'TOOL-SL-D.I' and code != 'WARM':
                        list.update({machine.execute_spend[day].getProgramCode(j): self.graph[search].gethight()})
                        self.graph[search].add_tick(machine.execute_spend[day].getProgramCode(j))  # set label with execute code to y-axis
                # use list to edit perday
                for j in range(machine.execute_spend[day].getProgramLength()):
                    if machine.execute_spend[day].getProgramCode(j) in list:
                        for k in range(int(machine.execute_spend[day].getStartSecond(j)+0.5),
                                       int(machine.execute_spend[day].getEndSecond(j)+0.5)):
                            perday[k] = list[machine.execute_spend[day].getProgramCode(j)]
                # print(color)
                self.graph[search].add_line(perday, color[-1], '--', 1, label_name + 'Execute')
                # ****plan section****
                # self.graph[search].add_tick('')
                perday = []                 # initialize perday
                for i in range(0, 86400):
                    perday.append(0)
                for k in range(len(machine.plan_spend)):
                    # find the day execute is handling, or do nothing in this day
                    if machine.execute_spend[day].getDay() == machine.plan_spend[k].getDay():
                        # find out all of execute codes, and mark them within plan_num
                        for j in range(machine.plan_spend[k].getProgramLength()):
                            if machine.plan_spend[k].getProgramCode(j) not in list:
                                list.update({machine.plan_spend[k].getProgramCode(j): self.graph[search].gethight()})
                                self.graph[search].add_tick(machine.plan_spend[k].getProgramCode(j))
                        # use list to edit perday
                        for j in range(machine.plan_spend[k].getProgramLength()):
                            for l in range(int(machine.plan_spend[k].getStartSecond(j) + 0.5),
                                           int(machine.plan_spend[k].getEndSecond(j) + 0.5)):
                                perday[l] = list[machine.plan_spend[k].getProgramCode(j)]
                self.graph[search].add_line(perday, color[-1], '-', 1, label_name + 'Expect')
                self.graph[search].add_tick('')
            color.pop()
