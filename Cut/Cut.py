from Cut.LoadData import LoadData
from Cut.WorkList import WorkList


class Cut:
    def __init__(self, load_file, plan_file):
        self.load_file = load_file
        self.plan_file = plan_file
        self.load_data = []
        self.plan_data = []
        self.split()

    def split(self):
        print(' ****Cut file into data****')
        for file in self.load_file:
            self.load_data.append(LoadData(file))
            print("     Load Data: " + self.load_data[-1].machine_name)
        for file in self.plan_file:
            self.plan_data.append(WorkList(file))
            print("     Work List: " + self.plan_data[-1].machine_name)
