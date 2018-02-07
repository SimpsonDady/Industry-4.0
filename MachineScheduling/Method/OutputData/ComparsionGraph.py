
class ComparsionGraph:

    skylineSame = []
    skylineDiff = []
    skylineNormal = []
    skylineImprove = []

    def dataComparsion(self):
        print('Create a DataGraph(Correlate)')

        print('1. Correlate ')
        print('2. AntiCorrelate ')
        print('3. Independent ')
        print('others. Break')
        xtype = input('Choose the data type : ')

        for num in range(1, 2, 1):                                                      # change here num
            tmp, ttmp, tmp2, ttmp2 = [], [], [], []
            tmpSkylineNormal, tmpSkylineImprove = [], []
            symbol_1, symbol_2 = [], []
            if xtype == '1':
                fn = open('D:/pythonScript/DecisionTree/Method/OutputData/Correlate/'+str(num)+'/DimSkyline.txt',
                         'r', encoding='UTF-8')
                fi = open('D:/pythonScript/DecisionTree/Method/OutputData/Correlate(Improve)/'+str(num)+'/DimSkyline(Improving).txt',
                         'r', encoding='UTF-8')
            elif xtype == '2':
                fn = open('D:/pythonScript/DecisionTree/Method/OutputData/AntiCorrelate/'+str(num)+'/DimSkyline.txt',
                         'r', encoding='UTF-8')
                fi = open('D:/pythonScript/DecisionTree/Method/OutputData/AntiCorrelate(Improve)/'+str(num)+'/DimSkyline(Improving).txt',
                         'r', encoding='UTF-8')
            elif xtype == '3':
                fn = open('D:/pythonScript/DecisionTree/Method/OutputData/Independent/'+str(num)+'/DimSkyline.txt',
                         'r', encoding='UTF-8')
                fi = open('D:/pythonScript/DecisionTree/Method/OutputData/Independent(Improve)/'+str(num)+'/DimSkyline(Improving).txt',
                         'r', encoding='UTF-8')
            else:
                break

            while True:
                x = fn.readline()
                if x == '':
                    break
                tmp.append(x)

            while True:
                y = fi.readline()
                if y == '':
                    break
                tmp2.append(y)

            fn.close()
            fi.close()

            for i in range(len(tmp)):
                ttmp.append(tmp[i].split())
                symbol_1.append(ttmp[i][0])

            for j in range(len(tmp2)):
                ttmp2.append(tmp2[j].split())
                symbol_2.append(ttmp2[j][0])

            self.skylineNormal.append(symbol_1)
            self.skylineImprove.append(symbol_2)

            s1 = set(symbol_1)
            s2 = set(symbol_2)
            resultDiff = list(s1.difference(s2))                                #相同的skyline #(s1-s2)
            resultSame = list(s1.intersection(s2))                              #不相同的skyline

            self.skylineSame.append(resultSame)
            self.skylineDiff.append(resultDiff)

        for num in range(0, 1, 1):                                              # change here num

            print('\n')
            PercentOfTheSame = "%.2f" % (len(self.skylineSame[num]) * 100 / len(self.skylineNormal[num]))
            PercentOfTheDiff = "%.2f" % (len(self.skylineDiff[num]) * 100 / len(self.skylineNormal[num]))
            print('在第'+str(num)+'個資料集中 : ')
            print('加速演算法 和 普通演算法 的相同比率', PercentOfTheSame, '%') # PercentOfTheSame
            print('加速演算法 和 普通演算法 的不同比率', PercentOfTheDiff, '%') # PercentOfTheDiff


c = ComparsionGraph()
c.dataComparsion()
print('\n')


'''
s1.symmetric_difference(s2) To Find All difference between s1 and s2
'''
# s1.symmetric_difference(s2)
# s1 ^ s2 (exclusive)
'''
Find the in s2 but not in s1
'''
#s1.difference(s2)
# s1 - s2