class Data:
    def __init__(self, program, component, worknumber, NC, version, workcenter,
                 machinename, startdate, starttime, enddate, endtime, spendtime):
        self.program = program
        self.component = component
        self.worknumber = worknumber
        self.nc = NC
        self.version = version
        self.workcenter = workcenter
        self.machinename = machinename
        self.startdate = startdate
        self.starttime = starttime
        self.enddate = enddate
        self.endtime = endtime
        self.spendtime = spendtime

    def getlist(self):
        return [self.program, self.component, self.worknumber, self.nc, self.version, self.workcenter,
                self.machinename, self.startdate, self.starttime, self.enddate, self.endtime, self.spendtime]
