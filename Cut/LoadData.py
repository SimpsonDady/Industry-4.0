import os


class LoadData:
    def __init__(self, file):
        self.machine_name = ''
        self.date = []                  # list of {'year', 'month', 'date'}
        self.time = []                  # list of {'hour', 'minute', 'second'}
        self.code = []                  # list of main program code
        self.work = []
        self.split(file)     # transform filename to name type ( str.format(name) )

    def split(self, file):
        next(file)      # Skip the header line
        for line in file:         # read line of fileObject
            cut = line.split('\t')                   # Split Line
            # split Machine Name
            if cut[0] == '9703':
                self.machine_name = 'DMG01'
            if cut[0] == '9702':
                self.machine_name = 'DMG02'
            if cut[0] == 'S001':
                self.machine_name = "STC01"
            # split date and time
            writetime = cut[1].split(' ')            # split load time
            cutdate = writetime[0].split('-')        # split date
            cuttime = writetime[1].split(':')        # split time
            self.date.append({"year": int(cutdate[0]), "month": int(cutdate[1]), "date": int(cutdate[2])})
            self.time.append({"hour": int(cuttime[0]), "minute": int(cuttime[1]), "second": float(cuttime[2])})
            # Split code
            if self.machine_name.startswith('DMG'):
                part = cut[2].split('\\')
                code = part[-1].split('_')  # Split main program code
                self.code.append(code[0])
            else:
                part = cut[2].split('_')
                self.code.append(part[2])

            # Split work status         # Split word status
            if self.machine_name.startswith('DMG'):
                status = 6
            else:
                status = 4
            if cut[status] == "START":
                self.work.append(1)
            else:
                self.work.append(0)
