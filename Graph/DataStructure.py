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
        return self.y_ticks.index(tick) + 1

    def add_alltime(self, allstart, allend, program):
        self.allstart = allstart
        self.allend = allend
        self.program = program

    def sort_y_tick(self, y_ticks):
        try:
            self.y_ticks.index(y_ticks)+1
        except ValueError:
            self.y_ticks.append(y_ticks)
        self.y_ticks = sorted(self.y_ticks)
        print(self.y_ticks)
