import math
from openpyxl import Workbook
from TimeModel.DataStructure import Data


class Build:
    def __init__(self, machine_name, execute_format, status_format):
        self.machine_name = machine_name
        self.execute_format = execute_format
        # self.plan_format = plan_format
        self.status_format = status_format
        self.ws = Workbook()
        self.wb = self.ws.active
        self.wb.append(['工具代碼', '刀號', '開始時間', '結束時間', '花費時間', '次數', '平均時間'])
        self.timemodel = []
        self.output()
        self.preday = 0
        self.prestartsecond = 0

    def output(self):
        startcode = 0
        startdate = 0
        endcode = 0
        enddate = 0

        for f in range(len(self.execute_format)):
            print(self.execute_format[f].prgram)
            filter = []
            count = {}
            for i in range(len(self.execute_format[f].knife)):
                if (self.execute_format[f].knife[i].end - self.execute_format[f].knife[i].start).total_seconds() < 400:
                    filter.append(self.execute_format[f].knife[i].knife)
                else:
                    if self.execute_format[f].knife[i].knife in count:
                        count[self.execute_format[f].knife[i].knife] += 1
                    else:
                        count.update({self.execute_format[f].knife[i].knife: 1})
            if f < len(self.execute_format)-1:
                count = {key: value for key, value in count.items() if key not in filter and self.execute_format[f+1].knife[0].knife != key}
                print(count)
            if len(list(count.values())) != 0:
                self.execute_format[f].count = list(count.values())[0]
                for key, value in count.items():
                    self.execute_format[f].count = math.gcd(self.execute_format[f].count, value)
                    self.execute_format[f].avg_time = self.execute_format[f].total_time.total_seconds() / self.execute_format[f].count
            else:
                self.execute_format[f].avg_time = 0
        for format in self.execute_format:
            for i in range(len(format.knife)):
                self.timemodel.append(Data(format.program, format.knife[i].knife,
                                           format.knife[i].start, format.knife[i].end,
                                           (format.knife[i].end - format.knife[i].start).total_seconds(), format.count, format.avg_time))
                self.wb.append(self.timemodel[-1].getlist())
            self.ws.save('D:\\result\\time_model\\' + self.machine_name + '_TimeModel.xlsx')

    # def save(self, startdate, startcode, enddate, endcode):
    #     worknumber = 0
    #     Nc = ''
    #     workcenter = 0
    #     component = ''
    #     version = ''
    #     for day in range(len(self.plan_format)):
    #         for j in range(len(self.plan_format[day].program)):
    #             if self.plan_format[day].program[j].code == self.execute_format[enddate].program[endcode].code:
    #                 worknumber = self.plan_format[day].program[j].worknumber
    #                 Nc = self.plan_format[day].program[j].nc
    #                 workcenter = self.plan_format[day].program[j].center
    #                 component = self.plan_format[day].program[j].component
    #                 version = self.plan_format[day].program[j].version
    #     self.timemodel.append(Data(self.execute_format[enddate].program[endcode].code, component, worknumber, Nc,
    #                                version, workcenter, self.machine_name, self.execute_format[startdate].day,
    #                                self.execute_format[startdate].program[startcode].startTime,
    #                                self.execute_format[enddate].day,
    #                                self.execute_format[enddate].program[endcode].endTime, time, counttime / 3600))
    #     self.wb.append(self.timemodel[-1].getlist())
