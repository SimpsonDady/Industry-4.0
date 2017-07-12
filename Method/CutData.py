from os import name


class CutData:
    def __init__(self, fn):
        self.date = []                  # list of {'year', 'month', 'date'}
        self.time = []                  # list of {'hour', 'minute', 'second'}
        self.code = []                  # list of main program code
        self.work = []
        self.split(fn.format(name))     # transform filename to name type ( str.format(name) )

    def split(self, filename):
        title = True
        with open(filename) as fileObject:  # open load data
            for line in fileObject:         # read line of fileObject
                if title:                   # skip Title line
                    title = False
                    continue
                cut = line.split('\t')                   # Split Line
                # Section2 time
                writetime = cut[1].split(' ')            # split load time
                cutdate = writetime[0].split('-')        # split date
                cuttime = writetime[1].split(':')        # split time
                self.time.append({"hour": int(cuttime[0]), "minute": int(cuttime[1]), "second": float(cuttime[2])})
                self.date.append({"year": int(cutdate[0]), "month": int(cutdate[1]), "date": int(cutdate[2])})
                # Section 3 code
                part = cut[2].split('\\')
                code = part[-1].split('_')      # Split main program code
                self.code.append(code[0])       # Save main program code
                # Section 6 work status         # Split word status
                if cut[6] == "START":
                    self.work.append(1)
                else:
                    self.work.append(0)
