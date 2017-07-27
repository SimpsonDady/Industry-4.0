from Format.DataStructure import Data


class LoadData:
    def __init__(self, date, time):
        self.date = date
        self.time = time

    def build(self, inputs):
        outputs = []  # To save the result of formatted data
        date = self.date[0]['date']  # Witch day is been handling
        pro = inputs[0]  # Witch program is been handling
        # handle first data before go into loop
        outputs.append(Data(self.date[0]['year'], self.date[0]['month'], self.date[0]['date']))
        outputs[-1].addProgram(pro)
        outputs[-1].setEnd(-1, self.time[0]['hour'], self.time[0]['minute'], self.time[0]['second'])
        for i in range(1, len(inputs)):
            # if read another date, than create a new object of Data
            if self.date[i]['date'] != date:
                outputs[-1].setStart(-1, self.time[i - 1]['hour'], self.time[i - 1]['minute'],
                                     self.time[i - 1]['second'])
                date = self.date[i]['date']
                pro = inputs[i]
                outputs.append(Data(self.date[i]['year'], self.date[i]['month'], self.date[i]['date']))
                outputs[-1].addProgram(pro)
                outputs[-1].setEnd(-1, self.time[i]['hour'], self.time[i]['minute'], self.time[i]['second'])
            # if read another program create another object of program (inside of original Data)
            if inputs[i] != pro:
                outputs[-1].setStart(-1, self.time[i - 1]['hour'], self.time[i - 1]['minute'],
                                     self.time[i - 1]['second'])
                pro = inputs[i]
                outputs[-1].addProgram(pro)
                outputs[-1].setEnd(-1, self.time[i]['hour'], self.time[i]['minute'], self.time[i]['second'])
        outputs[-1].setStart(-1, self.time[-1]['hour'], self.time[-1]['minute'], self.time[-1]['second'])
        return outputs
