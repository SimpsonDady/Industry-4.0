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
        warm = 0
        startcode = 0
        startdate = 0
        endcode = 0
        enddate = 0
        for i in range(len(self.execute_format)):
            for j in range(len(self.execute_format[i].program)):
                if self.execute_format[i].program[j].code.startswith('B', 0):
                    check = self.execute_format[i].program[j].code.replace('B', '2')
                    comment = check.isdigit()
                    # print(comment)
                elif self.execute_format[i].program[j].code.startswith('A', 0):
                    check = self.execute_format[i].program[j].code.replace('A', '1')
                    comment = check.isdigit()
                else:
                    comment = False

                if self.execute_format[startdate].date - self.execute_format[i].date > 1:
                    shut_down = True
                else:
                    shut_down = False

                if not comment:
                    startdate = i
                    startcode = j
                    continue
                elif self.execute_format[i].program[j].code == self.execute_format[enddate].program[endcode].code \
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
        worknumber = 0
        NC = ''
        workcenter = 0
        component = ''
        version = ''
        for day in range(len(self.plan_format)):
            for j in range(len(self.plan_format[day].program)):
                if self.plan_format[day].program[j].code == self.execute_format[enddate].program[endcode].code:
                    worknumber = self.plan_format[day].program[j].worknumber
                    NC = self.plan_format[day].program[j].nc
                    workcenter = self.plan_format[day].program[j].center
                    component = self.plan_format[day].program[j].component
                    version = self.plan_format[day].program[j].version
        # 扣除交接時間
        if self.execute_format[enddate].date == self.execute_format[startdate].date:
            startsecondcount = self.execute_format[startdate].program[startcode].startSecond
            endsecond = self.execute_format[enddate].program[endcode].endSecond
        else:
            startsecondcount = 0
            endsecond = self.execute_format[enddate].program[endcode].endSecond
        counttime = 0
        for date in range(enddate, startdate + 1):
            if date == startdate:
                startsecondcount = self.execute_format[startdate].program[startcode].startSecond
            for i in self.status_format:
                if i == self.status_format[date]:
                    for j in range(len(i.program)):
                        if i.program[j].startSecond >= startsecondcount and i.program[j].endSecond <= endsecond and \
                                        i.program[j].code == 0:  #  include
                            for k in range(int(i.program[j].startSecond + 0.5), int(i.program[j].endSecond + 0.5)):
                                if k in range(10800, 13800) or k in range(43200, 46800) or k in range(64800, 66600):
                                    counttime += 1
                        elif i.program[j].startSecond >= startsecondcount and i.program[j].code == 0: #  headinclude
                            if i.program[j].endSecond >= self.prestartsecond and self.predate == i.date:
                                for k in range(int(i.program[j].startSecond + 0.5), int(i.program[j].endSecond + 0.5)):
                                    if k in range(10800, 13800) or k in range(43200, 46800) or k in range(64800, 66600):
                                        if k >= self.prestartsecond:
                                            continue
                                        counttime += 1
                        elif i.program[j].endSecond <= endsecond and i.program[j].code == 0: #  tailinclude
                            for k in range(int(startsecondcount + 0.5), int(i.program[j].endSecond + 0.5)):
                                if k in range(10800, 13800) or k in range(43200, 46800) or k in range(64800, 66600):
                                    counttime += 1
                        elif i.program[j].startSecond <= startsecondcount and i.program[j].endSecond >= endsecond and \
                                        i.program[j].code == 0:  #  include
                            for k in range(int(startsecondcount + 0.5), int(endsecond + 0.5)):
                                if k in range(10800, 13800) or k in range(43200, 46800) or k in range(64800, 66600):
                                    counttime += 1
                    self.predate = i.date
                    self.prestartsecond = self.execute_format[startdate].program[startcode].startSecond
            endsecond = 86400
        print(counttime)
        time = (self.execute_format[enddate].program[endcode].endSecond
                - self.execute_format[startdate].program[startcode].startSecond) / 3600
        time += ((self.execute_format[enddate].date - self.execute_format[startdate].date) * 24)
        self.timemodel.append(Data(self.execute_format[enddate].program[endcode].code, component, worknumber, NC,
                                   version, workcenter, self.machine_name, self.execute_format[startdate].day,
                                   self.execute_format[startdate].program[startcode].startTime,
                                   self.execute_format[enddate].day,
                                   self.execute_format[enddate].program[endcode].endTime, time, counttime/3600))
        self.wb.append(self.timemodel[-1].getlist())
