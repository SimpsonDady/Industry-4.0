class Data:
    def __init__(self, program, count, max, min, mid, above, center, below, average, machinename):
        self.program = program
        self.count = count
        self.max = max
        self.min = min
        self.mid = mid
        self.above = above
        self.center = center
        self.below = below
        self.average = average
        self.machinename = machinename

    def getlist(self):
        return [self.machinename, self.program, self.count, self.min, self.below, self.max, self.above, self.mid,
                self.center, self.average]
