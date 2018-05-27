class Data:
    def __init__(self, component):
        self.component = component
        self.text = []
        self.filter = []
    def add_text(self, Word):
        self.text.append(Word)
    def add_filter(self, filter):
        self.filter.append(filter)
class Word:
    def __init__(self):
        self.word = []
    def add_knife(self, kinfe, startTime, endTime, filterlast):
        self.word.append(Kinfe(kinfe, startTime, endTime, filterlast))
class Kinfe:
    def __init__(self, kinfe, startTime, endTime, filterlast):
        self.startTime = startTime
        self.endTime = endTime
        self.kinfe = kinfe
        self.filterlast = filterlast