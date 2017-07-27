from Format.DataStructure import Data


class WorkList:
    def __init__(self, start_date, start_time, end_date, end_time):
        self.start_date = start_date
        self.start_time = start_time
        self.end_date = end_date
        self.end_time = end_time

    def build(self, inputs):
        outputs = []
        date = self.start_date[0]
        # handle first data before go into loop
        outputs.append(Data(self.start_date[0]['year'], self.start_date[0]['month'], self.start_date[0]['date']))
        outputs[0].addProgram(inputs[0])
        outputs[0].setStart(0, self.start_time[0]['hour'], self.start_time[0]['minute'], self.start_time[0]['second'])
        if date != self.end_date[0]:
            date = self.end_date[0]
            outputs[0].setEnd(0, 23, 59, 59)
            outputs.append(Data(self.end_date[0]['year'], self.end_date[0]['month'], self.end_date[0]['date']))
            outputs[0].addProgram(inputs[0])
            outputs[0].setStart(1, 0, 0, 0)
            outputs[0].setEnd(1, self.end_time[0]['hour'], self.end_time[0]['minute'], self.end_time[0]['second'])
        else:
            outputs[0].setEnd(0, self.end_time[0]['hour'], self.end_time[0]['minute'], self.end_time[0]['second'])
        for day in range(1, len(inputs)):
            # if read another date, than create a new object of Data
            if date != self.start_date[day]:
                outputs.append(Data(self.start_date[day]['year'],
                                    self.start_date[day]['month'], self.start_date[day]['date']))
                date = self.start_date[day]
            # Save the code and start time
            outputs[-1].addProgram(inputs[day])
            outputs[-1].setStart(-1, self.start_time[day]['hour'],
                                 self.start_time[day]['minute'], self.start_time[day]['second'])
            # if end date is not equals to start date, than let 23:59:59 be the end time,
            # and create a new object of data begin at 0:0:0 end at end time.
            # for example: 07-05 19:00 ~ 07-06 02:00 becomes 07-05 19:00~23:59 and 07-06 00:00~02:00
            if date != self.end_date[day]:
                date = self.end_date[day]
                outputs[-1].setEnd(-1, 23, 59, 59)
                outputs.append(Data(self.end_date[day]['year'],
                                    self.end_date[day]['month'], self.end_date[day]['date']))
                outputs[-1].addProgram(inputs[day])
                outputs[-1].setStart(-1, 0, 0, 0)
                outputs[-1].setEnd(-1, self.end_time[day]['hour'],
                                   self.end_time[day]['minute'], self.end_time[day]['second'])
            else:
                outputs[-1].setEnd(-1, self.end_time[day]['hour'],
                                   self.end_time[day]['minute'], self.end_time[day]['second'])
        return outputs
