# Loading the import
import matplotlib.pyplot as plt
import numpy as np


class TimeGraph:

    dataCorr = []
    dataAntiCorr = []
    dataIndependent = []
    timeCostCorrelate, timeCostAntiCorrelate, timeCostIndependent = [], [], []

    dataCorri = []                      # Improve algorithm
    dataAntiCorri = []
    dataIndependenti = []
    timeCostCorrelate_i, timeCostAntiCorrelate_i, timeCostIndependent_i = [], [], []

    heapCorr, heapAnti, heapIndep = [], [], []
    heapCorr1, heapAnti1, heapIndep1 = [], [], []
    timeCost_1, timeCost_2 = [], []

    def __init__(self):
        print('Create a TimeGraph')
        self.timeCostCorrelate, self.timeCostAntiCorrelate, self.timeCostIndependent = [], [], []
        # tmpCostCorrelate, tmpCostAntiCorrelate, tmpCostIndependent = [], [], []
        # tmpCostCorrelate_i, tmpCostAntiCorrelae_i, tmpCostIndependent_i = [], [], []
        #
        # tmp, tmp2, tmp3 = [], [], []
        # tmp4, tmp5, tmp6 = [], [], []

        for times in range(1, 11, 1):
            times = str(times)

            # Normal Data
            fr = open('D:/pythonScript/DecisionTree/Method/OutputData/Correlate(Normal)/'+times+'/DimCostTime.txt',
                      'r', encoding='UTF-8')
            fb = open('D:/pythonScript/DecisionTree/Method/OutputData/AntiCorrelate(Normal)/'+times+'/DimCostTime.txt',
                      'r', encoding='UTF-8')
            fg = open('D:/pythonScript/DecisionTree/Method/OutputData/Independent(Normal)/'+times+'/DimCostTime.txt',
                      'r', encoding='UTF-8')

            # Improved data
            fri = open('D:/pythonScript/DecisionTree/Method/OutputData/Correlate(Improve1)/'+times+'/DimCostTime(Improving).txt',
                      'r', encoding='UTF-8')
            fbi = open('D:/pythonScript/DecisionTree/Method/OutputData/AntiCorrelate(Improve1)/'+times+'/DimCostTime(Improving).txt',
                      'r', encoding='UTF-8')
            fgi= open('D:/pythonScript/DecisionTree/Method/OutputData/Independent(Improve1)/'+times+'/DimCostTime(Improving).txt',
                      'r', encoding='UTF-8')

            tmp, tmp2, tmp3 = [], [], []
            tmp4, tmp5, tmp6 = [], [], []

            while True:
                # Correlate(fr), AntiCorrelate(fb), Independent(fg)
                x, y, z = fr.readline(), fb.readline(), fg.readline()
                xi, yi, zi = fri.readline(), fbi.readline(), fgi.readline()
                if x == '':
                    break
                tmp.append(x), tmp2.append(y), tmp3.append(z)
                tmp4.append(xi), tmp5.append(yi), tmp6.append(zi)

            fr.close(), fb.close(), fg.close()
            fri.close(), fbi.close(), fgi.close()

            # print('tmp', tmp)
            # print('tmp2', tmp2)
            # print('tmp3', tmp3)

            tmpCostCorrelate, tmpCostAntiCorrelate, tmpCostIndependent = [], [], []
            tmpCostCorrelate_i, tmpCostAntiCorrelate_i, tmpCostIndependent_i = [], [], []

            for i in range(len(tmp)):
                tmpCostCorrelate.extend(tmp[i].split())
                tmpCostCorrelate_i.extend(tmp4[i].split())

                tmpCostAntiCorrelate.extend(tmp2[i].split())
                tmpCostAntiCorrelate_i.extend(tmp5[i].split())

                tmpCostIndependent.extend(tmp3[i].split())
                tmpCostIndependent_i.extend(tmp6[i].split())

            # print('c1', tmpCostCorrelate)
            # print('a1', tmpCostAntiCorrelate)
            # print('i1', tmpCostIndependent)

            self.timeCostCorrelate.append(tmpCostCorrelate)
            self.timeCostAntiCorrelate.append(tmpCostAntiCorrelate)
            self.timeCostIndependent.append(tmpCostIndependent)

            self.timeCostCorrelate_i.append(tmpCostCorrelate_i)
            self.timeCostAntiCorrelate_i.append(tmpCostAntiCorrelate_i)
            self.timeCostIndependent_i.append(tmpCostIndependent_i)
        # print('c2', len(self.timeCostCorrelate))
        # print('a2', self.timeCostAntiCorrelate)
        # print('i2', self.timeCostIndependent)


        self.dataCorr = self.calMeans(self.timeCostCorrelate)
        self.dataAntiCorr = self.calMeans(self.timeCostAntiCorrelate)
        self.dataIndependent = self.calMeans(self.timeCostIndependent)

        self.dataCorri = self.calMeans(self.timeCostCorrelate_i)
        self.dataAntiCorri = self.calMeans(self.timeCostAntiCorrelate_i)
        self.dataIndependenti = self.calMeans(self.timeCostIndependent_i)

    def createTimeCombineGraph(self):

        # change to rangeIndex
        rangeIndex = [4, 5, 6, 7, 8, 9, 10]
        plt.figure(figsize=(16, 10), dpi=80)

        plt.subplot(111)
        plt.plot(rangeIndex, self.dataCorr, marker='s', color='red', linewidth=2.5, linestyle='-', label='Correlation(DHSQA)')
        plt.plot(rangeIndex, self.dataAntiCorr, marker='o', color='blue', linewidth=2.5, linestyle='-', label='AntiCorrelation(DHSQA)')
        plt.plot(rangeIndex, self.dataIndependent, marker='^', color='green', linewidth=2.5, linestyle='-', label='Independence(DHSQA)')

        plt.plot(rangeIndex, self.dataCorri, marker='s', color='k', linewidth=2.5, linestyle='-', label='Correlation(EDHSQA)')
        plt.plot(rangeIndex, self.dataAntiCorri, marker='o', color='m', linewidth=2.5, linestyle='-', label='AntiCorrelation(EDHSQA)')
        plt.plot(rangeIndex, self.dataIndependenti, marker='^', color='c', linewidth=2.5, linestyle='-', label='Independence(EDHSQA)')

        plt.title('Plot of ALL', fontsize=12)
        plt.xlabel('Nodes', fontsize=12)
        plt.ylabel('Cost Time', fontsize=12)

        plt.legend(loc='upper left', frameon=False)
        plt.savefig('D:/pythonScript/DecisionTree/Figure/DimCostComparison/Mix/CombineTimeGraph.png.png', dpi=300)

        plt.show()

    def DimCompareTime(self):
        plt.figure(figsize=(16, 10), dpi=80)
        plt.subplot(111)
        # change to rangeIndex
        rangeIndex = [4, 5, 6, 7, 8, 9, 10]

        plt.plot(rangeIndex, self.dataCorr, marker='s', color='blue', linewidth=2.5, linestyle='-', label='Correlation')
        plt.plot(rangeIndex, self.dataAntiCorr, marker='o', color='red', linewidth=2.5, linestyle='-', label='AntiCorrelation')
        plt.plot(rangeIndex, self.dataIndependent, marker='^', color='green', linewidth=2.5, linestyle='-', label='Independence')

        plt.title('DHSQA', fontsize=12)
        plt.xlabel('Nodes Found (number)', fontsize=12)
        plt.ylabel('Cost Time (sec)', fontsize=12)
        plt.legend(loc='upper left', frameon=False)

        plt.savefig('D:/pythonScript/DecisionTree/Figure/DimCostComparison/Improve/TimeComparison.png', dpi=300)
        plt.show()

    def DimHeapCompareHeap(self):
        plt.figure(figsize=(16, 10), dpi=80)
        plt.subplot(111)
        # change to rangeIndex
        rangeIndex = [4, 5, 6, 7, 8, 9, 10]

        plt.plot(rangeIndex, self.heapCorr, marker='s', color='red', linewidth=2.5, linestyle='-',
                 label='Correlation')
        plt.plot(rangeIndex, self.heapAnti, marker='o', color='blue', linewidth=2.5, linestyle='-',
                 label='AntiCorrelation')
        plt.plot(rangeIndex, self.heapIndep, marker='^', color='green', linewidth=2.5, linestyle='-',
                 label='Independence')

        plt.title('DHSQA', fontsize=12)
        plt.xlabel('Nodes Found (number)', fontsize=12)
        plt.ylabel('MAX of Heap', fontsize=12)
        plt.legend(loc='upper left', frameon=False)

        plt.savefig('D:/pythonScript/DecisionTree/Figure/DimCostComparison/Normal/HeapComparison.png', dpi=300)
        plt.show()


    def calMeans(self, argc):
        tmpList = argc
        meanList = []

        for i in range(0, 7, 1):
            costTime = []
            for j in range(0, len(tmpList), 1):
                costTime.append(tmpList[j][i])
            means = 0.0
            for k in range(len(costTime)):
                means += float(costTime[k])
            meanList.append((means/10))
        return meanList

t = TimeGraph()

#t.DimCompareTime()
t.createTimeCombineGraph()