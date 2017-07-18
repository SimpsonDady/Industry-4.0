from DMG.Method.Data import Data


class Format:
    def __init__(self, date, time):
        self.date = date
        self.time = time
    # Python has no override, thus we use default input to comply that

    def build(self, inputs, component='', version='', start_date=None, start_time=None, end_date=None, end_time=None):
        # Only input one variable (For workSpend and programSpend)
        if start_date is None and start_time is None and end_date is None and end_time is None:
            outputs = []                    # To save the result of formatted data
            date = self.date[0]['date']     # Witch day is been handling
            pro = inputs[0]                 # Witch program is been handling
            # handle first data before go into loop
            outputs.append(Data(self.date[0]['year'], self.date[0]['month'], self.date[0]['date']))
            outputs[-1].addProgram(pro)
            outputs[-1].setEnd(-1, self.time[0]['hour'], self.time[0]['minute'], self.time[0]['second'])
            for i in range(1, len(inputs)):
                # if read another date, than create a new object of Data
                if self.date[i]['date'] != date:
                    outputs[-1].setStart(-1, self.time[i-1]['hour'], self.time[i-1]['minute'], self.time[i-1]['second'])
                    date = self.date[i]['date']
                    pro = inputs[i]
                    outputs.append(Data(self.date[i]['year'], self.date[i]['month'], self.date[i]['date']))
                    outputs[-1].addProgram(pro)
                    outputs[-1].setEnd(-1, self.time[i]['hour'], self.time[i]['minute'], self.time[i]['second'])
                # if read another program create another object of program (inside of original Data)
                if inputs[i] != pro:
                    outputs[-1].setStart(-1, self.time[i-1]['hour'], self.time[i-1]['minute'], self.time[i-1]['second'])
                    pro = inputs[i]
                    outputs[-1].addProgram(pro)
                    outputs[-1].setEnd(-1, self.time[i]['hour'], self.time[i]['minute'], self.time[i]['second'])
                if component != '' and version != '':
                    if component[i] != '' and version[i] != '':
                        outputs[-1].setInformation(-1, component[i], version[i])
            outputs[-1].setStart(-1, self.time[-1]['hour'], self.time[-1]['minute'], self.time[-1]['second'])
            return outputs
        # input all of the variables (For workSpend)
        elif start_date is not None and start_time is not None and end_date is not None and end_time is not None:
            outputs = []
            date = start_date[0]
            # handle first data before go into loop
            outputs.append(Data(start_date[0]['year'], start_date[0]['month'], start_date[0]['date']))
            outputs[0].addProgram(inputs[0])
            outputs[0].setStart(0, start_time[0]['hour'], start_time[0]['minute'], start_time[0]['second'])
            if date != end_date[0]:
                date = end_date[0]
                outputs[0].setEnd(0, 23, 59, 59)
                outputs.append(Data(end_date[0]['year'], end_date[0]['month'], end_date[0]['date']))
                outputs[0].addProgram(inputs[0])
                outputs[0].setStart(1, 0, 0, 0)
                outputs[0].setEnd(1, end_time[0]['hour'], end_time[0]['minute'], end_time[0]['second'])
            else:
                outputs[0].setEnd(0, end_time[0]['hour'], end_time[0]['minute'], end_time[0]['second'])
            for day in range(1, len(inputs)):
                # if read another date, than create a new object of Data
                if date != start_date[day]:
                    outputs.append(Data(start_date[day]['year'], start_date[day]['month'], start_date[day]['date']))
                    date = start_date[day]
                # Save the code and start time
                outputs[-1].addProgram(inputs[day])
                outputs[-1].setStart(-1, start_time[day]['hour'], start_time[day]['minute'], start_time[day]['second'])
                # if end date is not equals to start date, than let 23:59:59 be the end time,
                # and create a new object of data begin at 0:0:0 end at end time.
                # for example: 07-05 19:00 ~ 07-06 02:00 becomes 07-05 19:00~23:59 and 07-06 00:00~02:00
                if date != end_date[day]:
                    date = end_date[day]
                    outputs[-1].setEnd(-1, 23, 59, 59)
                    outputs.append(Data(end_date[day]['year'], end_date[day]['month'], end_date[day]['date']))
                    outputs[-1].addProgram(inputs[day])
                    outputs[-1].setStart(-1, 0, 0, 0)
                    outputs[-1].setEnd(-1, end_time[day]['hour'], end_time[day]['minute'], end_time[day]['second'])
                else:
                    outputs[-1].setEnd(-1, end_time[day]['hour'], end_time[day]['minute'], end_time[day]['second'])
            return outputs
        else:
            try:
                raise IOError('Please Enter 1 or 4 input, others amount is not allowed')
            except IOError:
                raise
