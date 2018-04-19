class Data:
    def __init__(self, program, knife, start, end, execute, count, time):
        self.program = program
        self.knife = knife
        self.start = start
        self.end = end
        self.execute = execute
        self.count = count
        self.time = time

    def getlist(self):
        return [self.program, self.knife, self.start, self.end, self.execute, self.count, self.time]
