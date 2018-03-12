from Format.LoadData import LoadData
from Format.WorkList import WorkList


class Format:
    def __init__(self, load_data, plan_data):
        self.load_data = load_data
        self.plan_data = plan_data
        self.machine_name = []
        self.match = []
        self.status_format = []
        self.execute_format = []
        self.plan_format = []
        self.format()

    def format(self):
        print("****Form data into format****")
        for data in self.load_data:
            self.match.append(-1)
            self.machine_name.append(data.machine_name)
            for i in range(len(self.plan_data)):
                if self.plan_data[i].machine_name == data.machine_name:
                    self.match[-1] = i
            load = LoadData(data.time)
            self.status_format.append(load.build(data.work, data.sub, data.line))
            print('     Status format: ' + data.machine_name)
            self.execute_format.append(load.build(data.code, data.sub, data.line))
            print('     Execute format: ' + data.machine_name)
        for data in self.plan_data:
            plan = WorkList(data.start_date, data.start_time, data.end_date, data.end_time, data.version,
                            data.component, data.work_num, data.nc, data.center)
            self.plan_format.append(plan.build(data.code))
            print('     Plan format: ' + data.machine_name)

        for exe in self.execute_format:
            for program in exe:
                program.print_all()

        # print(self.match)
        # for i in self.match:
        #     if self.match[i] == -1:
        #         print('     Missing Work List: ' + self.machine_name[i])
