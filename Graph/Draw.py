import matplotlib.pyplot as plt
import numpy as np
import time

import sys


class Draw:
    def __init__(self, graph):
        self.graph = graph
        self.draw()

    def draw(self):
        for day in range(len(self.graph)):
            for i in range(len(self.graph[day].lines)):
                plt.plot(self.graph[day].lines[i].line, color=self.graph[day].lines[i].color,
                         linestyle=self.graph[day].lines[i].style, linewidth=self.graph[day].lines[i].width,
                         label=self.graph[day].lines[i].label)
            plt.title(self.graph[day].day)             # Edit title
            plt.xlabel('Time', fontsize=10, fontweight='bold')      # Edit X-label
            plt.legend(loc='upper center', ncol=int(len(self.graph[day].lines) / 2 + 0.5), fontsize=6)
            # mark hour at x-axis and code at y-axis
            plt.xticks(np.arange(0, 86401, 3600), range(0, 25), fontsize=10, rotation='horizontal')
            plt.yticks(range(0, self.graph[day].y_high), self.graph[day].y_ticks, fontsize=8, rotation='horizontal')
            # draw horizontal line at every hour
            x0 = 0
            for i in range(1, 26, 1):
                plt.plot([x0, x0, ], [0, self.graph[day].y_high, ], 'k-', linewidth=0.2)
                x0 = x0+3600
            # save the graph with the name of it's self.graph[day] and set the dpi of the graph
            plt.savefig('D:\\result\\graph\\' + self.graph[day].day, dpi=180)
            print('\r  (' + str(day + 1) + '/' + str(len(self.graph)) + ')' + self.graph[day].day + '.png', end='')
            # time.sleep(1)
            plt.close('all')
