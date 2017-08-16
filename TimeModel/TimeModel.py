from Statistics.Statistics import Statistics
from TimeModel.Bulid import Build
from TimeModel.DataBase import DataBase


class Timemodel:
    def __init__(self, machine_name, match, execute_format, plan_format, status_format):
        self.model = []
        print("****Build format into TimesModel****")
        for i in range(len(execute_format)):
            build = Build(machine_name[i], execute_format[i], plan_format[match[i]], status_format[i])
            self.model.append(build.timemodel)
            print('     TimesModel: ' + machine_name[i])
        # DataBase(self.build)

        statistics = Statistics(self.model)
