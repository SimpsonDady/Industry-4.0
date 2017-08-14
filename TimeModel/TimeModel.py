from TimeModel.Bulid import Build
from TimeModel.DataBase import DataBase


class Timemodel:
    def __init__(self, machine_name, match, execute_format, plan_format, status_format):
        print("****Build format into TimesModel****")
        for i in range(len(execute_format)):
            build = Build(machine_name[i], execute_format[i], plan_format[match[i]], status_format[i])
            print('     TimesModel: ' + machine_name[i])
        DataBase(build)
