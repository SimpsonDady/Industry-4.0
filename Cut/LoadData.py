from datetime import datetime
from time import sleep


class LoadData:
    def __init__(self, file):
        self.machine_name = ''
        self.time = []
        self.code = []  # list of main program code
        self.work = []
        self.sub = []
        self.line = []
        self.knife = []
        self.split(file)  # transform filename to name type ( str.format(name) )

    def split(self, file):
        next(file)  # Skip the header line
        for line in file:  # read line of fileObject
            cut = line.split('\t')  # Split Line
            # split Machine Name
            if cut[0] == '9703':
                self.machine_name = 'DMG01'
            if cut[0] == '9702':
                self.machine_name = 'DMG02'
            if cut[0] == 'S001':
                self.machine_name = "STC01"
            # Split date and time
            try:
                self.time.append(datetime.strptime(cut[1], "%Y-%m-%d %H:%M:%S.%f"))
            except ValueError:
                self.time.append(datetime.strptime(cut[1], "%Y-%m-%d %H:%M:%S"))
            # Split code
            if self.machine_name.startswith('DMG'):
                part = cut[2].split('\\')
                code = part[-1].split('_')  # Split main program code
                self.code.append(code[0])
                self.sub.append(code[-1])
            else:
                part = cut[2].split('_')
                # print(self.date[-1], end=' ')
                # print(self.time[-1])
                self.code.append(part[2])
                self.sub.append(part[-2])
            # Split work status         # Split word status
            if self.machine_name.startswith('DMG'):
                status = 6
            else:
                status = 4
            if cut[status] == "START":
                self.work.append(1)
            else:
                self.work.append(0)

            # Split line
            self.line.append(int(cut[4]))

            # Split knife
            self.knife.append(int(cut[11]))
