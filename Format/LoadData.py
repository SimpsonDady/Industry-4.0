from Format.DataStructure import Data


class LoadData:
    def __init__(self, time):
        self.time = time

    def build(self, program, knife):
        outputs = []  # To save the result of formatted data
        # handle first data before go into loop
        j = 0
        while knife[j] == 0:
            j += 1
        outputs.append(Data(program[j], knife[j], self.time[j]))
        pre_program = program[j]
        pre_knife = knife[j]
        for i in range(j+1, len(program)):
            if knife[i] == 0:
                continue
            if knife[i] != pre_knife or program[i] != pre_program:
                outputs[-1].set_start(self.time[i-1])
                outputs.append(Data(program[i], knife[i], self.time[i]))
                pre_knife = knife[i]
                pre_program = program[i]
        outputs[-1].set_start(self.time[-1])
        return outputs
