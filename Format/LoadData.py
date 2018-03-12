from Format.DataStructure import Data


class LoadData:
    def __init__(self, time):
        self.time = time

    def build(self, program, sub_program, line):
        outputs = []  # To save the result of formatted data
        sub = sub_program[0]    # Witch Sub program is been handling
        ln = line[0]            # Witch line is been handling
        # handle first data before go into loop
        outputs.append(Data(program[0], sub_program[0], self.time[0]))
        for i in range(1, len(program)):
            if line[i] == 0:
                continue
            if (sub_program[i] == sub and line[i] < ln) or sub_program[i] != sub:
                outputs[-1].set_start(self.time[i-1])
                outputs.append(Data(program[i], sub_program[i], self.time[0]))
                sub = sub_program[i]
                ln = line[i]
            # if read another date, than create a new object of Data
            '''if self.date[i]['date'] != date:
                outputs[-1].setStart(-1, self.time[i - 1]['hour'], self.time[i - 1]['minute'],
                                     self.time[i - 1]['second'])
                date = self.date[i]['date']
                pro = program[i]
                outputs.append(Data(self.date[i]['year'], self.date[i]['month'], self.date[i]['date']))
                outputs[-1].addProgram(pro)
                outputs[-1].setEnd(-1, self.time[i]['hour'], self.time[i]['minute'], self.time[i]['second'])
            # if read another program create another object of program (inside of original Data)
            if program[i] != pro:
                outputs[-1].setStart(-1, self.time[i - 1]['hour'], self.time[i - 1]['minute'],
                                     self.time[i - 1]['second'])
                pro = program[i]
                outputs[-1].addProgram(pro)
                outputs[-1].setEnd(-1, self.time[i]['hour'], self.time[i]['minute'], self.time[i]['second'])'''
        outputs[-1].set_start(self.time[-1])
        return outputs
