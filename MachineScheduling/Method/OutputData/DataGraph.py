import matplotlib.pyplot as plt
from Method.Kmedoids_Point import Kmedoids
from Method.Math.Math import Math

class DataGraph:

    k = Kmedoids()
    m = Math()

    #print('Create a DataGraph(Correlate)')
    def nodeCorrelateScatter(self):
        print('Create a DataGraph(Correlate)')

        nsymbol, nvalue, npoint, allnode = self.k.Kmedoids(5)

        plt.figure(figsize=(8, 6), dpi=80)
        plt.subplot(111)
        plt.scatter(nvalue[0], npoint[0], marker='s', color='r', linewidth=0.1, linestyle='-', label='class_1')
        plt.scatter(nvalue[1], npoint[1], marker='o', color='b', linewidth=0.1, linestyle='-', label='class_2')
        plt.scatter(nvalue[2], npoint[2], marker='^', color='g', linewidth=0.1, linestyle='-', label='class_3')
        plt.scatter(nvalue[3], npoint[3], marker='>', color='m', linewidth=0.1, linestyle='-', label='class_4')
        plt.scatter(nvalue[4], npoint[4], marker='<', color='c', linewidth=0.1, linestyle='-', label='class_5')

        for i in range(len(allnode)):
            plt.annotate(allnode[i].symbol, xy=(allnode[i].droneValue, allnode[i].dronePoint))

        plt.title('DataScatter_Graph(Correlate)', fontsize=12)
        plt.xlabel('droneDistance', fontsize=12)
        plt.ylabel('dronePoint', fontsize=12)
        plt.legend(loc='upper right', frameon=False)

        plt.savefig('D:/pythonScript/DecisionTree/Figure/Scatter/CorrelateScatter.png', dpi=300)
        plt.show()

    #print('Create a DataGraph(AntiCorrelate)')
    def nodeAntiCorrelateScatter(self):
        print('Create a DataGraph(AntiCorrelate)')

        nsymbol, nvalue, npoint = self.k.Kmedoids(3)

        plt.figure(figsize=(8, 6), dpi=80)
        plt.subplot(111)
        plt.scatter(nvalue[0], npoint[0], marker='s', color='r', linewidth=0.1, linestyle='-', label='class_1')
        plt.scatter(nvalue[1], npoint[1], marker='o', color='b', linewidth=0.1, linestyle='-', label='class_2')
        plt.scatter(nvalue[2], npoint[2], marker='^', color='g', linewidth=0.1, linestyle='-', label='class_3')
        plt.title('DataScatter_Graph(AntiCorrelate)', fontsize=12)
        plt.xlabel('droneDistance', fontsize=12)
        plt.ylabel('dronePoint', fontsize=12)
        plt.legend(loc='upper right', frameon=False)

        plt.savefig('D:/pythonScript/DecisionTree/Figure/Scatter/AntiCorrelateScatter.png', dpi=300)
        plt.show()

    #print('Create a DataGraph(Independent)')
    def nodeIndependentScatter(self):
        print('Create a DataGraph(Independent)')

        nsymbol, nvalue, npoint = self.k.Kmedoids(3)

        plt.figure(figsize=(8, 6), dpi=80)
        plt.subplot(111)
        plt.scatter(nvalue[0], npoint[0], marker='s', color='r', linewidth=0.1, linestyle='-', label='class_1')
        plt.scatter(nvalue[1], npoint[1], marker='o', color='b', linewidth=0.1, linestyle='-', label='class_2')
        plt.scatter(nvalue[2], npoint[2], marker='^', color='g', linewidth=0.1, linestyle='-', label='class_3')
        plt.title('DataScatter_Graph(Independent)', fontsize=12)
        plt.xlabel('droneDistance', fontsize=12)
        plt.ylabel('dronePoint', fontsize=12)
        plt.legend(loc='upper right', frameon=False)

        plt.savefig('D:/pythonScript/DecisionTree/Figure/Scatter/IndependentScatter.png', dpi=300)
        plt.show()

    def xynodeCorrelateScatter(self):
        print('Create a xy_DataGraph(Correlate)')
        f = open('D:/pythonScript/DecisionTree/Data/NodeDataCorrelate.txt', 'r', encoding='utf-8')
        tmp, tmp2 = [], []
        tmpxlocation, tmpylocation = [], []
        xlocation, ylocation = [], []

        while True:
            x = f.readline()
            if x == '':
                break
            tmp.append(x)

        for i in range(len(tmp)):
            tmp2.append(tmp[i].split())
            tmpxlocation.append(float(tmp2[i][1]))
            tmpylocation.append(float(tmp2[i][2]))

        for i in range(len(tmp)):
            # Normalization
            xlocation.append(self.m.Normalization(tmpxlocation[i], tmpxlocation))
            ylocation.append(self.m.Normalization(tmpylocation[i], tmpylocation))

        f.close()

        plt.figure(figsize=(8, 6), dpi=80)
        plt.subplot(111)
        plt.scatter(xlocation, ylocation, marker='s', color='r', linewidth=0.1, linestyle='-', label='class_1')

        for i in range(10):
            plt.annotate(i, xy=(xlocation[i], ylocation[i]))

        plt.title('XY_DataScatter_Graph(Correlate)', fontsize=12)
        plt.xlabel('droneDistance', fontsize=12)
        plt.ylabel('dronePoint', fontsize=12)
        plt.legend(loc='upper right', frameon=False)

        plt.savefig('D:/pythonScript/DecisionTree/Figure/xyLocation/xyLocationCorrelateScatter.png', dpi=300)
        plt.show()

d = DataGraph()
d.nodeCorrelateScatter()
#d.nodeAntiCorrelateScatter()
#d.nodeIndependentScatter()
#d.xynodeCorrelateScatter()