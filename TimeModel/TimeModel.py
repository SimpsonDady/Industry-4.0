from TimeModel.Bulid import Build

class Timemodel:
    def __init__(self, machine_name, match, execute_format, plan_format):
        print(match)
        for i in range(len(execute_format)):
            build = Build(machine_name[i], execute_format[i], plan_format[match[i]])
