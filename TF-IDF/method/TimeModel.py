from collections import Counter
from datetime import datetime

import math
from openpyxl import Workbook


class TimeModel:
    def __init__(self, Data):
        self.data = Data
        self.ws = Workbook()
        self.wb = self.ws.active
        self.wb.append(['工具代碼', '刀號', '開始時間', '結束時間', '花費時間', '次數', '平均時間'])
        self.timemodel()
    def timemodel(self):
        for data in self.data:
            print(data.component)
            print(data.filter)
            for text in data.text:
                knife = []
                starttime = []
                allstarttime = []
                endtime = []
                allendtime = []
                for i in text:
                    if (i.endTime - i.startTime).total_seconds() < 100:
                        continue
                    if i.kinfe in data.filter:
                        allstarttime.append(i.startTime)
                        allendtime.append(i.endTime)
                        continue
                    if i.filterlast == False:
                        knife.append(i.kinfe)
                    starttime.append(i.startTime)
                    endtime.append(i.endTime)
                    allstarttime.append(i.startTime)
                    allendtime.append(i.endTime)
                count = Counter(knife)
                print(count)
                gcdcount = list(count.values())[0]
                for i in count.values():
                    gcdcount = math.gcd(gcdcount, i)
                if gcdcount < min(list(count.values())):
                    gcdcount = min(list(count.values()))
                for i in range(len(knife)):
                    self.wb.append([data.component, int(knife[i]), starttime[i], endtime[i], str((endtime[i] - starttime[i]).total_seconds()), gcdcount, str((allendtime[0] - allstarttime[-1]).total_seconds() / gcdcount)])
        self.ws.save('D:\\result\\time_model\\' + "DMG_1" + '_TimeModelPart2.xlsx')