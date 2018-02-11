from Scheduling.OrderData import OrderData


class ScheduledData(OrderData):
    def __init__(self, data, start_time):
        super(ScheduledData, self).__init__(data.workId, data.machineId, data.costTime, data.receive, data.deadline)
        self.startTime = start_time
        self.finishTime = start_time + self.costTime * 60 * 60
        denominator = self.deadline - self.receive
        self.schedule = (self.deadline - self.startTime) / denominator
        self.arrive = (self.finishTime - self.receive) / denominator
        if self.arrive > 1:
            self.arrive = 1 - self.arrive
        # self.delay = self.deadline - self.finishTime
        # if self.delay < 0:
        #     self.delay = 0
