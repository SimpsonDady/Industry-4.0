
class OutputData:

    def writeTime2Txt(self, argc, type, pathType):
        # type = ['Coorelate', 'Anti_Coorelate', 'Independent']
        if type == 0:
            f = open('D:/pythonScript/MachineScheduling/Method/OutputData/OutputData(bruteforce)/'+pathType+'/DimCostTime.txt',
                     'w', encoding='UTF-8')
        elif type == 1:
            f = open('D:/pythonScript/MachineScheduling/Method/OutputData/OutputData(Normal)/'+pathType+'/DimCostTime.txt',
                     'w', encoding='UTF-8')
        data = argc

        for i in range(0, len(data), 1):
            for j in range(0, len(data[i]), 1):
                f.write(str(data[i][j]))
                if j != len(data[i]) - 1:
                    f.write('\n')

        f.close()

    def writeData2Txt(self, argc, type, pathType):
        # type = ['Coorelate', 'Anti_Coorelate', 'Independent']
        if type == 0:
            f = open('D:/pythonScript/MachineScheduling/Method/OutputData/OutputData(btuteforce)/'+pathType+'/DimSkyline.txt', 'w',
                     encoding='UTF-8')
        if type == 1:
            f = open('D:/pythonScript/MachineScheduling/Method/OutputData/OutputData(Normal)/'+pathType+'/DimSkyline.txt', 'w',
                     encoding='UTF-8')
        data = argc

        for i in range(0, len(data), 1):
            for j in range(0, len(data[i]), 1):
                f.write(str(data[i][j].symbol) + ' ' +
                        str(data[i][j].adim) + ' ' +
                        str(data[i][j].bdim) + ' ' +
                        str(data[i][j].cdim) + ' ' +
                        str(data[i][j].ddim) + ' ' +
                        str(data[i][j].edim))
                if j != len(data[i]) - 1:
                    f.write('\n')
            if i != len(data) - 1:
                f.write('\n')
        f.close()

    def writeHeapTxt(self, argc, type, pathType):
        # type = ['Coorelate', 'Anti_Coorelate', 'Independent']
        if type == 1:
            f = open('D:/pythonScript/MachineScheduling/Method/OutputData/OutputData(Normal)/'+pathType+'/DimHeap.txt',
                     'w', encoding='UTF-8')
        data = argc

        for i in range(0, len(data), 1):
            for j in range(0, len(data[i]), 1):
                f.write(str(data[i][j]))
                if j != len(data[i]) - 1:
                    f.write('\n')
        f.close()
