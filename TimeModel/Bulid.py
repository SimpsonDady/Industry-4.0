from openpyxl import Workbook
from TimeModel.DataStructure import Data


class Build:
    def __init__(self, machine_name, execute_format, plan_format):
        self.machine_name = machine_name
        self.execute_format = execute_format
        self.plan_format = plan_format
        self.ws = Workbook()
        self.wb = self.ws.active
        self.wb.append(['工具代碼', '件號', '工號', 'NC程式', '版別', '工作中心', '機台編號',
                        '開始日期', '開始時間', '結束日期', '結束時間', '加工工時'])
        self.timemodel = []
        self.output()

    def output(self):
        warm = 0
        startcode = 0
        startdate = 0
        endcode = 0
        enddate = 0
        for i in range(len(self.execute_format)):
            for j in range(self.execute_format[i].getProgramLength()):
                if self.execute_format[i].getProgramCode(j).startswith('B', 0):
                    check = self.execute_format[i].getProgramCode(j).replace('B', '2')
                    comment = check.isdigit()
                    # print(comment)
                elif self.execute_format[i].getProgramCode(j).startswith('A', 0):
                    check = self.execute_format[i].getProgramCode(j).replace('A', '1')
                    comment = check.isdigit()
                else:
                    comment = False

                if self.execute_format[startdate].getDate() - self.execute_format[i].getDate() > 1:
                    shut_down = True
                else:
                    shut_down = False

                if not comment:
                    startdate = i
                    startcode = j
                    continue
                elif self.execute_format[i].getProgramCode(j) == self.execute_format[enddate].getProgramCode(endcode) \
                        and not shut_down:
                    startdate = i
                    startcode = j
                else:
                    self.save(startdate, startcode, enddate, endcode)
                    startdate = i
                    startcode = j
                    enddate = i
                    endcode = j
        self.save(startdate, startcode, enddate, endcode)
        self.ws.save('D:\\result\\time_model\\' + self.machine_name + '_TimeModel.xlsx')

    def save(self, startdate, startcode, enddate, endcode):
        worknum = 'N/A'
        NC = 'N/A'
        workcenter = 'N/A'
        component = 'N/A'
        version = 'N/A'
        for day in range(len(self.plan_format)):
            for j in range(self.plan_format[day].getProgramLength()):
               if self.plan_format[day].getProgramCode(j) == self.execute_format[enddate].getProgramCode(endcode):
                    worknum = self.plan_format[day].getWorknum(j)
                    NC = self.plan_format[day].getNc(j)
                    workcenter = self.plan_format[day].getCenter(j)
                    component = self.plan_format[day].getComponent(j)
                    version = self.plan_format[day].getVersion(j)
        time = (self.execute_format[enddate].getEndSecond(endcode)
                - self.execute_format[startdate].getStartSecond(startcode)) / 3600
        time += (self.execute_format[enddate].getDate() - self.execute_format[startdate].getDate()) * 24
        self.timemodel.append(Data(self.execute_format[enddate].getProgramCode(endcode), component, worknum, NC,
                                   version, workcenter, self.machine_name, self.execute_format[startdate].getDay(),
                                   self.execute_format[startdate].getStartTime(startcode),
                                   self.execute_format[enddate].getDay(),
                                   self.execute_format[enddate].getEndTime(endcode), time))
        self.wb.append(self.timemodel[-1].getlist())
