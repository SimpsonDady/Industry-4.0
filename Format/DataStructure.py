from datetime import datetime


class Knife:
    def __init__(self, knife, end_time):
        self.knife = knife
        self.component = ''
        self.version = ''
        self.worknumber = ''
        self.nc = ''
        self.center = ''
        self.start = datetime.min
        self.end = end_time

    def set_start(self, time):
        self.start = time

    def set_information(self, component, version, worknumber, nc, center):
        self.component = component
        self.version = version
        self.worknumber = worknumber
        self.nc = nc
        self.center = center

    def print_all(self):
        print(self.knife)
        print(self.start)
        print(self.end)
        print()



class Data:
    def __init__(self, program):
        self.program = program
        self.total_time = datetime.min
        self.avg_time = datetime.min
        self.count = 0
        self.knife = []

    def add_knife(self, knife, end_time):
        self.knife.append(Knife(knife, end_time))

    def set_start(self, time):
        self.knife[-1].start = time
        self.total_time = self.knife[0].end - self.knife[-1].start

    def set_information(self, component, version, worknumber, nc, center):
        self.knife[-1].set_information(component, version, worknumber, nc, center)

# class Data:
#     def __init__(self, sub_program):
#         self.
#         self.program = []
#
#     def addProgram(self, programCode):
#         self.program.append(Program(programCode))
#
#     def setStart(self, index, hour, minute, second):
#         self.program[index].setStart(hour, minute, second)
#
#     def setEnd(self, index, hour, minute, second):
#         self.program[index].setEnd(hour, minute, second)
#
#     def setInformation(self, index, component, version, worknumber, nc, center):
#         self.program[index].setInformation(component, version, worknumber, nc, center)
#
#     def printAll(self):
#         print(self.day)
#         for program in self.program:
#             print(program.getProgramCode())
#             print(program.getStartTime())
#             print(program.getEndTime())
#             print(program.getComponent())
#             print(program.getVersion())
