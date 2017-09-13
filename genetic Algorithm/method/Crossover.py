import random

from struct import unpack, pack


class Crossover:
    def __init__(self, data, mon, filter):
        self.data = data
        self.mon = mon
        self.filter = filter
        self.childMlist = []
        self.childSlist = []
        self.crossover()

    def crossover(self):
        for i in range(200):
            kidnum = random.randint(1, 200)
            monM = self.transform(self.mon[0])
            monS = self.transform(self.mon[1])
            seedM = self.transform(self.data['child' + str(kidnum)][0])
            seedS = self.transform(self.data['child' + str(kidnum)][1])

            if self.filter:
                monM2 = self.transform(self.mon[2])
                monS2 = self.transform(self.mon[3])
                seedM2 = self.transform(self.data['child' + str(kidnum)][2])
                seedS2 = self.transform(self.data['child' + str(kidnum)][3])

            if len(monM) > len(seedM):
                for i in range(len(monM) - len(seedM)):
                    seedM.insert(0, '0')
            elif len(monM) < len(seedM):
                for j in range(len(seedM) - len(monM)):
                    monM.insert(0, '0')
            index = random.randint(1, len(monM))
            childM = monM[:index] + seedM[index:]

            if len(monS) > len(seedS):
                for i in range(len(monS) - len(seedS)):
                    seedS.insert(0, '0')
            elif len(monS) < len(seedS):
                for j in range(len(seedS) - len(monS)):
                    monS.insert(0, '0')
            index = random.randint(1, len(monS))
            childS = monS[:index] + seedS[index:]

            self.childMlist.append(childM)
            self.childSlist.append(childS)
            if self.filter:
                if len(monM2) > len(seedM2):
                    for i in range(len(monM2) - len(seedM2)):
                        seedM2.insert(0, '0')
                elif len(monM2) < len(seedM2):
                    for j in range(len(seedM2) - len(monM2)):
                        monM2.insert(0, '0')
                index = random.randint(1, len(monM2))
                childM2 = monM2[:index] + seedM2[index:]

                if len(monS2) > len(seedS2):
                    for i in range(len(monS2) - len(seedS2)):
                        seedS2.insert(0, '0')
                elif len(monS2) < len(seedS2):
                    for j in range(len(seedS2) - len(monS2)):
                        monS2.insert(0, '0')
                index = random.randint(1, len(monS2))
                childS2 = monS2[:index] + seedS2[index:]

                self.childMlist.append(childM2)
                self.childSlist.append(childS2)
            # print("交配")

    def transform(self, num):
        change = []
        a = bin(unpack('I', pack('f', num))[0])
        for x in a[2:]:
            change.append(x)
        return change
