class Data:
    def __init__(self, program, knife, start, end):
        self.program = program
        self.knife = knife
        self.start = start
        self.end = end

    def getlist(self):
        return [self.program, self.knife, self.start, self.end]
