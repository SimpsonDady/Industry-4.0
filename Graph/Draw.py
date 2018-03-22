
import matplotlib.pyplot as plt
import numpy as np
import os
import time


class Draw:
    def __init__(self, graph):
        self.graph = graph
        self.draw()

    def draw(self):
        count = 0
        for day in self.graph:
            count += 1
            print(len(day.lines))
            line = []
            for i in range(len(day.lines)):
                line.append(day.lines[i].line)
            print(line)
            plt.plot(line, color='red',
                 linestyle='-', linewidth='0.5')
            plt.title(day.program)  # Edit title
            plt.xlabel('Time', fontsize=10, fontweight='bold')  # Edit X-label
            # plt.legend(loc='upper center', ncol=int(len(day.lines) / 2 + 0.5), fontsize=6)
            plt.yticks(range(1, len(day.y_ticks)+1), day.y_ticks, fontsize=8, rotation='horizontal')
            if os.path.exists('D:\\result\\graph\\'+day.program+ '\\'):
                plt.savefig('D:\\result\\graph\\' + day.program +"\\" + day.program + "picture" + str(count) + ".png", dpi=180)
            else:
                os.makedirs('D:\\result\\graph\\' + day.program)
                plt.savefig('D:\\result\\graph\\' + day.program + "\\" + day.program + "picture" + str(count) + ".png",
                            dpi=180)
            plt.close('all')
