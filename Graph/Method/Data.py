class Line:
    def __init__(self, line, color, style, width, label):
        self.__line = line
        self.__color = color
        self.__style = style
        self.__width = width
        self.__label = label

    def getline(self):
        return self.__line

    def getstyle(self):
        return self.__style

    def getcolor(self):
        return self.__color

    def getwidth(self):
        return self.__width

    def getlabel(self):
        return self.__label


class Data:
    def __init__(self, day):
        self.__day = day
        self.__y_high = 1
        self.__y_ticks = ['Stop']
        self.__lines = []

    def add_line(self, line, color, style, width, label):
        self.__lines.append(Line(line, color, style, width, label))

    def add_tick(self, tick):
        self.__y_ticks.append(tick)
        self.__y_high += 1

    def getday(self):
        return self.__day

    def gethight(self):
        return self.__y_high

    def getticks(self):
        return self.__y_ticks

    def getlinelength(self):
        return len(self.__lines)

    def getline(self, index):
        return self.__lines[index].getline()

    def getstyle(self, index):
        return self.__lines[index].getstyle()

    def getcolor(self, index):
        return self.__lines[index].getcolor()

    def getwidth(self, index):
        return self.__lines[index].getwidth()

    def getlabel(self, index):
        return self.__lines[index].getlabel()
