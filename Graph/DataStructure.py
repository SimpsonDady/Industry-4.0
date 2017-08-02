class Line:
    def __init__(self, line, color, style, width, label):
        self.line = line
        self.color = color
        self.style = style
        self.width = width
        self.label = label


class Data:
    def __init__(self, day):
        self.day = day
        self.y_high = 1
        self.y_ticks = ['Stop']
        self.lines = []

    def add_line(self, line, color, style, width, label):
        self.lines.append(Line(line, color, style, width, label))

    def add_tick(self, tick):
        self.y_ticks.append(tick)
        self.y_high += 1
