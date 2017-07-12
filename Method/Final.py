import matplotlib.pyplot as plt
import numpy as np


class Final:
    def __init__(self, run_spend, program_spend, work_spend):
        self.run_spend = run_spend
        self.work_spend = work_spend
        self.program_spend = program_spend

        self.work = []      # Line of work in Graph
        self.program = []   # Line of program in Graph
        self.run = []       # Line of run in Graph
        self.high = []      # Graph's height
        self.draw()

    def draw(self):
        ytick = []  # label of y-axis
        # program major
        for day in range(len(self.program_spend)):
            # ****run section****
            perday = []                 # To save one line in a day
            for i in range(0, 86400):   # 1 day = 86400 seconds
                perday.append(0)
            ytick.append(['Stop', 'Run'])   # set label 0 and 1 to y-axis
            # if read 1, than let perday in range of start to end become 1
            for j in range(self.run_spend[day].getProgramLength()):
                if self.run_spend[day].getProgramCode(j) == 1:
                    for k in range(int(self.run_spend[day].getStartSecond(j)),
                                   int(self.run_spend[day].getEndSecond(j))):
                        perday[k] = 1
            self.run.append(perday)
            # ****program section****
            program_num = 2      # start with 2 (run use 0,1)
            program_list = {}    # let every program code have a number
            perday = []          # initialize perday
            for i in range(0, 86400):
                perday.append(0)
            # find out all of program codes, and mark them within program_num
            for j in range(self.program_spend[day].getProgramLength()):
                code = self.program_spend[day].getProgramCode(j)
                if code not in program_list and code != 'TOOL-SL-D.I' and code != 'WARM':
                    program_list.update({self.program_spend[day].getProgramCode(j): program_num})
                    program_num += 1
                    ytick[-1].append(self.program_spend[day].getProgramCode(j))  # set label with program code to y-axis
            # use program_list to edit perday
            for j in range(self.program_spend[day].getProgramLength()):
                if self.program_spend[day].getProgramCode(j) in program_list:
                    for k in range(int(self.program_spend[day].getStartSecond(j)+0.5),
                                   int(self.program_spend[day].getEndSecond(j)+0.5)):
                        perday[k] = program_list[self.program_spend[day].getProgramCode(j)]
            self.program.append(perday)
            # ****work section****
            work_num = program_num + 1  # start with max of program_num +1 (separate in one label)
            ytick[-1].append('')
            work_list = {}
            perday = []                 # initialize perday
            for i in range(0, 86400):
                perday.append(0)
            for k in range(len(self.work_spend)):
                # find the day program is handling, or do nothing in this day
                if self.program_spend[day].getDay() == self.work_spend[k].getDay():
                    # find out all of program codes, and mark them within work_num
                    for j in range(self.work_spend[k].getProgramLength()):
                        if self.work_spend[k].getProgramCode(j) not in work_list:
                            work_list.update({self.work_spend[k].getProgramCode(j): work_num})
                            ytick[-1].append(self.work_spend[k].getProgramCode(j))
                            work_num += 1
                    # use work_list to edit perday
                    for j in range(self.work_spend[k].getProgramLength()):
                        for l in range(int(self.work_spend[k].getStartSecond(j) + 0.5),
                                       int(self.work_spend[k].getEndSecond(j) + 0.5)):
                            perday[l] = work_list[self.work_spend[k].getProgramCode(j)]
            self.work.append(perday)
            self.high.append(work_num)      # record the highest label in y-axis

        for day in range(len(self.program)):
            plt.plot(self.work[day], color='g', linewidth=1)        # Graph work line
            plt.plot(self.program[day], color='b', linewidth=1)     # Graph program line
            plt.plot(self.run[day], color='r', linewidth=0.5)       # Graph run line
            plt.title(self.program_spend[day].getDay())             # Edit title
            plt.xlabel('Time', fontsize=10, fontweight='bold')      # Edit X-label
            plt.xticks(np.arange(0, 86401, 3600), range(0, 25), fontsize=8, rotation='horizontal') # mark hour at x-axis
            plt.yticks(range(0, self.high[day]), ytick[day], fontsize=8, rotation='horizontal')    # mark code at y-axis
            # draw horizontal line at every hour
            x0 = 0
            for i in range(1, 26, 1):
                plt.plot([x0, x0, ], [0, self.high[day], ], 'k-', linewidth=0.2)
                x0 = x0+3600
            # save the graph with the name of it's day and set the dpi of the graph
            plt.savefig(self.program_spend[day].getDay(), dpi=1080)
            print(self.program_spend[day].getDay() + '.png')
            plt.close('all')
