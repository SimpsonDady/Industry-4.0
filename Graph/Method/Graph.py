import matplotlib.pyplot as plt
import numpy as np


class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.draw()

    def draw(self):
        print('Graphing...')
        for day in self.graph:
            for i in range(day.getlinelength()):
                plt.plot(day.getline(i), color=day.getcolor(i), linewidth=day.getwidth(i))        # Graph plan line
            plt.title(day.getday())             # Edit title
            plt.xlabel('Time', fontsize=10, fontweight='bold')      # Edit X-label
            # mark hour at x-axis and code at y-axis
            plt.xticks(np.arange(0, 86401, 3600), range(0, 25), fontsize=8, rotation='horizontal')
            plt.yticks(range(0, day.gethight()), day.getticks(), fontsize=8, rotation='horizontal')
            # draw horizontal line at every hour
            x0 = 0
            for i in range(1, 26, 1):
                plt.plot([x0, x0, ], [0, day.gethight(), ], 'k-', linewidth=0.2)
                x0 = x0+3600
            # save the graph with the name of it's day and set the dpi of the graph
            plt.savefig(day.getday(), dpi=180)
            print(day.getday() + '.png')
            plt.close('all')
        print('done')
