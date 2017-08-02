class Program:
    def __init__(self, p):
        self.code = p
        self.component = ''
        self.version = ''
        self.worknumber = ''
        self.nc = ''
        self.center = ''
        self.start = {'hour': -1, 'minute': -1, 'second': -1}
        self.end = {'hour': -1, 'minute': -1, 'second': -1}
        self.startTime = ''
        self.endTime = ''
        self.startSecond = -1
        self.endSecond = -1

    def setStart(self, h, m, s):
        self.start['hour'] = h
        self.start['minute'] = m
        self.start['second'] = s
        self.startSecond = (h * 60 + m) * 60 + s
        self.startTime = str(h) + ':' + str(m) + ':' + str(s)

    def setEnd(self, h, m, s):
        self.end['hour'] = h
        self.end['minute'] = m
        self.end['second'] = s
        self.endSecond = (h * 60 + m) * 60 + s
        self.endTime = str(h) + ':' + str(m) + ':' + str(s)

    def setInformation(self, component, version, worknumber, nc, center):
        self.component = component
        self.version = version
        self.worknumber = worknumber
        self.nc = nc
        self.center = center


class Data:
    def __init__(self, year, month, date):
        self.year = year
        self.month = month
        self.date = date
        self.day = str(year) + '-' + str(month) + '-' + str(date)
        self.program = []

    def addProgram(self, programCode):
        self.program.append(Program(programCode))

    def setStart(self, index, hour, minute, second):
        self.program[index].setStart(hour, minute, second)

    def setEnd(self, index, hour, minute, second):
        self.program[index].setEnd(hour, minute, second)

    def setInformation(self, index, component, version, worknumber, nc, center):
        self.program[index].setInformation(component, version, worknumber, nc, center)

    def printAll(self):
        print(self.day)
        for program in self.program:
            print(program.getProgramCode())
            print(program.getStartTime())
            print(program.getEndTime())
            print(program.getComponent())
            print(program.getVersion())
