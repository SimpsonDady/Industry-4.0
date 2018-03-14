from Format.DataStructure import Data


class WorkList:
    def __init__(self, start_time, end_time, version, component, work_num, nc, center):
        self.start_time = start_time
        self.end_time = end_time
        self.version = version
        self.component = component
        self.work_num = work_num
        self.nc = nc
        self.center = center

    def build(self, program):
        outputs = []
        for i in range(len(program)):
            outputs.append(Data(program, '', self.end_time[i]))
            outputs[-1].set_start(self.start_time[i])
            outputs[-1].set_information(self.component[i], self.version[i], self.work_num[i], self.nc[i], self.center[i])
        return outputs
