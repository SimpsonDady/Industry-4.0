from Graph.DataStructure import Data


class Daily:
    def __init__(self, machine_name, match, status_format, execute_format ,plan_format):
        self.machine_name = machine_name
        self.match = match
        self.status_format = status_format
        self.execute_format = execute_format
        self.plan_format = plan_format
        self.graph = []
        self.__draw(True)
        print('  Graph of machine dependence')
        self.__draw(False)
        print('  Graph of daily dependence')

    def __draw(self, independent):
        color = ['magenta', 'blue', 'red']
        for machine in range(len(self.execute_format)):
            if independent:
                machine_name = self.machine_name[machine] + '_'
                label_name = ''
            else:
                machine_name = ''
                label_name = self.machine_name[machine] + '_'
            # execute major
            for day in range(len(self.execute_format[machine])):
                search = -1
                for i in range(len(self.graph)):
                    if self.execute_format[machine][day].day == self.graph[i].day:
                        search = i
                if search == -1:
                    self.graph.append(Data(machine_name + self.execute_format[machine][day].day))
                # ****status section****
                if independent:
                    perday = []                 # To save one line in a day
                    for i in range(0, 86400):   # 1 day = 86400 seconds
                        perday.append(0)
                    self.graph[search].add_tick('Run')
                    # if read 1, than let perday in range of start to end become 1
                    for j in range(len(self.status_format[machine][day].program)):
                        if self.status_format[machine][day].program[j].code == 1:
                            for k in range(int(self.status_format[machine][day].program[j].startSecond + 0.5),
                                           int(self.status_format[machine][day].program[j].endSecond + 0.5)):
                                perday[k] = 1
                    self.graph[search].add_line(perday, 'black', '-', 0.5, 'Status')
                # ****execute section****
                list = {}    # let every execute code have a number
                perday = []          # initialize perday
                for i in range(0, 86400):
                    perday.append(0)
                # find out all of execute codes, and mark them within execute_num
                for j in range(len(self.execute_format[machine][day].program)):
                    code = self.execute_format[machine][day].program[j].code
                    if code.startswith('B', 0):
                        check = code.replace('B', '2')
                        confirm = check.isdigit()
                        # print(confirm)
                    elif code.startswith('A', 0):
                        check = code.replace('A', '1')
                        confirm = check.isdigit()
                    else:
                        confirm = False
                    if code not in list and confirm:
                        list.update({self.execute_format[machine][day].program[j].code: self.graph[search].y_high})
                        self.graph[search].add_tick(self.execute_format[machine][day].program[j].code)  # set label with execute code to y-axis
                # use list to edit perday
                for j in range(len(self.execute_format[machine][day].program)):
                    if self.execute_format[machine][day].program[j].code in list:
                        for k in range(int(self.execute_format[machine][day].program[j].startSecond + 0.5),
                                       int(self.execute_format[machine][day].program[j].endSecond + 0.5)):
                            perday[k] = list[self.execute_format[machine][day].program[j].code]
                # print(color)
                self.graph[search].add_line(perday, color[-1], '--', 1, label_name + 'Execute')
                # ****plan section****
                if self.match[machine] != -1:
                    perday = []                 # initialize perday
                    for i in range(0, 86400):
                        perday.append(0)
                    for k in range(len(self.plan_format[self.match[machine]])):
                        # find the day execute is handling, or do nothing in this day
                        if self.execute_format[machine][day].day == self.plan_format[machine][k].day:
                            # find out all of execute codes, and mark them within plan_num
                            for j in range(len(self.plan_format[machine][k].program)):
                                if self.plan_format[machine][k].program[j].code not in list:
                                    list.update({self.plan_format[machine][k].program[j].code: self.graph[search].y_high})
                                    self.graph[search].add_tick(self.plan_format[machine][k].program[j].code)
                            # use list to edit perday
                            for j in range(len(self.plan_format[machine][k].program)):
                                for l in range(int(self.plan_format[machine][k].program[j].startSecond + 0.5),
                                               int(self.plan_format[machine][k].program[j].endSecond + 0.5)):
                                    perday[l] = list[self.plan_format[machine][k].program[j].code]
                    self.graph[search].add_line(perday, color[-1], '-', 1, label_name + 'Expect')
                    self.graph[search].add_tick('')
            color.pop()
