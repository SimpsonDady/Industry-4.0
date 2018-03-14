from Format.DataStructure import Data


class LoadData:
    def __init__(self, time):
        self.time = time

    def build(self, program, sub_program, line):
        outputs = []  # To save the result of formatted data
        pre_sub = 'fuck'
        pre_line = -1
        last_line = line[0]
        # handle first data before go into loop
        outputs.append(Data(program[0], sub_program[0], self.time[0]))
        for i in range(1, len(program)):
            # if line[i] == 0:
            #     continue
            if program[i] == program[-1] and line[i] > last_line:
                outputs[-1].set_start(self.time[i-1])
                outputs.append(Data(program[i], sub_program[i], self.time[i]))
            elif sub_program[i] != sub_program[i-1]:
                if sub_program[i] == pre_sub and line[i] < pre_line:
                    # print('pop: ', self.time[i], ' ', outputs[-1].subProgram)
                    outputs.pop()
                    pre_sub = 'fuck'
                    pre_line = -1
                else:
                    outputs[-1].set_start(self.time[i-1])
                    outputs.append(Data(program[i], sub_program[i], self.time[i]))
                    pre_sub = sub_program[i-1]
                    pre_line = last_line
            if line[i] != 0:
                last_line = line[i]
        outputs[-1].set_start(self.time[-1])
        return outputs
