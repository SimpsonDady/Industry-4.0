import copy

from Scheduling.ScheduledData import ScheduledData


class Node:
    def __init__(self, data):
        self.scheduledData = []
        self.scheduledData.append(ScheduledData(copy.copy(data), data.receive))
        self.minSchedule = self.scheduledData[0].schedule
        self.avgSchedule = self.scheduledData[0].schedule
        self.minArrive = self.scheduledData[0].arrive
        self.avgArrive = self.scheduledData[0].arrive
        # self.minDelay = self.scheduledData[0].delay
        # self.avgDelay = self.scheduledData[0].delay

    def copy(self):
        copy = Node(self.scheduledData[0])
        for sd in self.scheduledData:
            copy.add_data(sd)
        return copy

    def add_data(self, data):
        # If Data already append to this node, skip this add motion
        for sd in self.scheduledData:
            if sd.workId == data.workId:
                return False

        if data.receive > self.scheduledData[-1].finishTime:
            self.scheduledData.append(ScheduledData(data, data.receive))
        else:
            self.scheduledData.append(ScheduledData(data, self.scheduledData[-1].finishTime))
        # Refresh the Attribute of this Node
        if self.scheduledData[-1].schedule < self.minSchedule:
            self.minSchedule = self.scheduledData[-1].schedule
        if self.scheduledData[-1].arrive < self.minArrive:
            self.minArrive = self.scheduledData[-1].arrive
        # if self.scheduledData[-1].delay < self.minDelay:
        #     self.minDelay = self.scheduledData[-1].delay
        length = len(self.scheduledData) - 1
        self.avgSchedule = (self.avgSchedule * length + self.scheduledData[-1].schedule) / (length + 1)
        self.avgArrive = (self.avgArrive * length + self.scheduledData[-1].arrive) / (length + 1)
        # self.avgDelay = (self.avgDelay * length + self.scheduledData[-1].delay) / (length + 1)
        return True

    def dominate(self, node):
        if node.minSchedule > self.minSchedule and node.avgSchedule > self.avgSchedule and \
                node.minArrive > self.minArrive and node.avgArrive > self.avgArrive:
            return True
        return False
        # or node.minDelay < self.minDelay or node.avgDelay < self.avgDelay

    def get_sum(self):
        return -(self.minSchedule + self.minArrive + self.avgArrive + self.avgSchedule)
        # + self.avgDelay + self.minDelay

    def print_path(self):
        for sd in self.scheduledData:
            print(sd.workId, end='->')
            # print(sd.startTime, end='%')
            # print(sd.workId, end='%')
            # print(sd.finishTime, end='->')
        print()

    def print_element(self):
        print('MinSchedule: ' + str(self.minSchedule) + '\nAvgSchedule: ' + str(self.avgSchedule) + '\nMinArrive: ' +
              str(self.minArrive) + '\nAvgArrive: ' + str(self.avgArrive))
        # + '\nMinDelay: ' + str(self.minDelay) + '\nAvgDelay: ' + str(self.avgDelay))
