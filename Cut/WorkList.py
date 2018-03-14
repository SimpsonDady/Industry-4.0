from datetime import datetime


class WorkList:
    def __init__(self, file):
        self.machine_name = ''
        self.start_time = []
        self.end_time = []
        self.code = []  # list of main program code
        self.component = []
        self.work_num = []
        self.nc = []
        self.version = []
        self.center = []
        self.split(file)

    def split(self, file):
        xlsx = file['Sheet1']  # Excel page
        for line in range(2, xlsx.max_row + 1):  # read row (line)
            for section in range(1, xlsx.max_column + 1):  # read column
                data = str(xlsx.cell(row=line, column=section).value)  # read one data
                if section == 1:
                    # self.machine_name = data
                    if data.startswith('DMG') and data.endswith('1'):
                        self.machine_name = 'DMG01'
                    elif data.startswith('DMG') and data.endswith('2'):
                        self.machine_name = 'DMG02'
                    else:
                        self.machine_name = 'STC01'
                if section == 2:
                    self.work_num.append(data)
                if section == 4:
                    self.center.append(data)
                if section == 5:  # Save start time(5)
                    self.start_time.append(datetime.strptime(data, "%Y-%m-%d %H:%M:%S"))
                if section == 6:  # Save end time(6)
                    self.end_time.append(datetime.strptime(data, "%Y-%m-%d %H:%M:%S"))
                if section == 7:
                    self.component.append(data)
                if section == 10:
                    self.nc.append(data)
                if section == 11:
                    self.version.append(data)
                if section == 13:  # main program code(13)
                    self.code.append(data)
