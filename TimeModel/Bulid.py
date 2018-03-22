from openpyxl import Workbook
from TimeModel.DataStructure import Data


class Build:
    def __init__(self, machine_name, execute_format, plan_format, status_format):
        self.machine_name = machine_name
        self.execute_format = execute_format
        self.plan_format = plan_format
        self.status_format = status_format
        self.ws = Workbook()
        self.wb = self.ws.active
        self.wb.append(['工具代碼', '件號', '工號', 'NC程式', '版別', '工作中心', '機台編號',
                        '開始日期', '開始時間', '結束日期', '結束時間', '加工工時', '換班時間'])
        self.timemodel = []
        self.output()
        self.preday = 0
        self.prestartsecond = 0

    def output(self):
        startcode = 0
        startdate = 0
        endcode = 0
        enddate = 0
        for i in range(len(self.execute_format)):
            self.timemodel.append(Data(self.execute_format[i].program, self.execute_format[i].knife, self.execute_format[i].start, self.execute_format[i].end))
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
