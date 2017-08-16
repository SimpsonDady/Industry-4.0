from openpyxl import Workbook

from Statistics.DataStructure import Data


class Statistics:
    def __init__(self, build):
        self.ws = Workbook()
        self.wb = self.ws.active
        self.wb.append(['機台編號', '工具代碼', '總數量', '最小值', '過小數量', '最大值', '過大數量', '中間值',
                        '合理數量', '平均'])
        self.statisticsmodel = []
        for time_model in build:
            self.count(time_model)

    def count(self, time_model):
        program_list = []
        program_data = []
        for p in time_model:
            if p.program not in program_list:
                program_list.append(p.program)
            machinename = p.machinename
        for i in program_list:
            for p in time_model:
                if i == p.program:
                    program_data.append(p.spendtime - p.shift)
            above = 0
            below = 0
            program_data.sort()
            min = program_data[0]
            max = program_data[-1]
            findmid = program_data[0]
            count = 0
            compare = {}
            averagelist = []
            for j in program_data:
                if int(j + 0.5) == int(findmid + 0.5):
                    count += 1
                else:
                    compare.update({int(findmid + 0.5): count})
                    findmid = j
                    count = 1
            compare.update({int(findmid + 0.5): count})
            valuecount = 0
            keycount = 0
            for key, value in compare.items():
                if value >= valuecount:
                    valuecount = value
                    keycount = key
            mid = keycount
            for k in program_data:
                if (mid - 2) <= k <= (mid + 2):
                    averagelist.append(k)
                if mid - 2 >= k:
                    below += 1
                elif mid + 2 <= k:
                    above += 1
                    calculate = k
                    temp = k
                    for l in range(int(calculate + 0.5)):
                        if calculate < 2:
                            for times in range(l - 1):
                                temp /= mid
                            if (mid - 2) <= int((k / int(temp)) + 0.5) <= (mid + 2):
                                averagelist.append(k / int(temp))
                            break
                        calculate /= mid
            center = len(averagelist)
            average = sum(averagelist) / len(averagelist)
            self.statisticsmodel.append(
                Data(i, len(program_data), max, min, mid, above, center, below, average, machinename))
            self.wb.append(self.statisticsmodel[-1].getlist())
            self.ws.save('D:\\result\\time_model\\' + '_StatisticsModel.xlsx')
            averagelist = []
            compare = {}
            program_data = []
            above = 0
            below = 0
