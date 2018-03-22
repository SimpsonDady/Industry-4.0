class Line:
    def __init__(self, line, style, width):
        self.line = line
        self.style = style
        self.width = width

class Data:
    def __init__(self):
        self.y_ticks = []
        self.lines = []
        self.program = ''
        self.allstart = 0
        self.allend = 0

    def add_line(self, line, style, width):
        self.lines.append(Line(line, style, width))

    def add_tick(self, tick):
        try:
            return self.y_ticks.index(tick)+1
        except ValueError:
            self.y_ticks.append(tick)
            return len(self.y_ticks)

    def add_alltime(self, allstart, allend, program):
        self.allstart = allstart
        self.allend = allend
        self.program = program
