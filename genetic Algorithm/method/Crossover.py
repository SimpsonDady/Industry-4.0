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
        for i in range(800):
            kidnum = random.randint(1, 800)
            monM = list(bin(int(self.mon[0]))[2:])
            monMdot = self.transform(self.mon[0]-int(self.mon[0]))
            monS = list(bin(int(self.mon[1]))[2:])
            monSdot = self.transform(self.mon[1]-int(self.mon[1]))
            seedM = list(bin(int(self.data['child' + str(kidnum)][0]))[2:])
            seedMdot = self.transform(self.data['child' + str(kidnum)][0] - int(self.data['child' + str(kidnum)][0]))
            seedS = list(bin(int(self.data['child' + str(kidnum)][1]))[2:])
            # print(self.data['child' + str(kidnum)][1])
            seedSdot = self.transform(self.data['child' + str(kidnum)][1]-int(self.data['child' + str(kidnum)][1]))

            if self.filter:
                monM2 = list(bin(int(self.mon[2]))[2:])
                monM2dot = self.transform(self.mon[2] - int(self.mon[2]))
                monS2 = list(bin(int(self.mon[3]))[2:])
                monS2dot = self.transform(self.mon[3] - int(self.mon[3]))
                seedM2 = list(bin(int(self.data['child' + str(kidnum)][2]))[2:])
                seedM2dot = self.transform(self.data['child' + str(kidnum)][2]-int(self.data['child' + str(kidnum)][2]))
                seedS2 = list(bin(int(self.data['child' + str(kidnum)][3]))[2:])
                seedS2dot = self.transform(self.data['child' + str(kidnum)][3] - int(self.data['child' + str(kidnum)][3]))

            if len(monM) > len(seedM):
                for i in range(len(monM) - len(seedM)):
                    seedM.insert(0, '0')
            elif len(monM) < len(seedM):
                for j in range(len(seedM) - len(monM)):
                    monM.insert(0, '0')
            if len(monMdot) > len(seedMdot):
                for i in range(len(monMdot) - len(seedMdot)):
                    seedMdot.insert(0, '0')
            elif len(monMdot) < len(seedMdot):
                for j in range(len(seedMdot) - len(monMdot)):
                    monMdot.insert(0, '0')
            indexdot = random.randint(1, len(monMdot))
            index = random.randint(1, len(monM))
            childM = monM[:index] + seedM[index:]
            childMdot = monMdot[:indexdot] + seedMdot[indexdot:]
            m = int("".join(map(str, childM)), 2)
            mdot = '0b' + ''.join(childMdot)

            if len(monS) > len(seedS):
                for i in range(len(monS) - len(seedS)):
                    seedS.insert(0, '0')
            elif len(monS) < len(seedS):
                for j in range(len(seedS) - len(monS)):
                    monS.insert(0, '0')
            if len(monSdot) > len(seedSdot):
                for i in range(len(monSdot) - len(seedSdot)):
                    seedSdot.insert(0, '0')
            elif len(monSdot) < len(seedSdot):
                for j in range(len(seedSdot) - len(monSdot)):
                    monSdot.insert(0, '0')
            index = random.randint(1, len(monS))
            childS = monS[:index] + seedS[index:]
            indexdot = random.randint(1, len(monSdot))
            childSdot = monSdot[:indexdot] + seedSdot[indexdot:]
            s = int("".join(map(str, childS)), 2)
            sdot = '0b' + ''.join(childSdot)
            self.childMlist.append(m+self.transformDec(mdot))
            self.childSlist.append(s+self.transformDec(sdot))


            if self.filter:
                if len(monM2) > len(seedM2):
                    for i in range(len(monM2) - len(seedM2)):
                        seedM2.insert(0, '0')
                elif len(monM2) < len(seedM2):
                    for j in range(len(seedM2) - len(monM2)):
                        monM2.insert(0, '0')
                if len(monM2dot) > len(seedM2dot):
                    for i in range(len(monM2dot) - len(seedM2dot)):
                        seedM2dot.insert(0, '0')
                elif len(monM2dot) < len(seedM2dot):
                    for j in range(len(seedM2dot) - len(monM2dot)):
                        monM2dot.insert(0, '0')
                # print(monM2)
                # print(seedM2)
                index = random.randint(1, len(monM2))
                childM2 = monM2[:index] + seedM2[index:]
                indexdot = random.randint(1, len(monM2dot))
                childM2dot = monM2dot[:indexdot] + seedM2dot[indexdot:]
                m2 = int("".join(map(str, childM2)), 2)
                m2dot = '0b' + ''.join(childM2dot)

                if len(monS2) > len(seedS2):
                    for i in range(len(monS2) - len(seedS2)):
                        seedS2.insert(0, '0')
                elif len(monS2) < len(seedS2):
                    for j in range(len(seedS2) - len(monS2)):
                        monS2.insert(0, '0')
                if len(monS2dot) > len(seedS2dot):
                    for i in range(len(monS2dot) - len(seedS2dot)):
                        seedS2dot.insert(0, '0')
                elif len(monS2dot) < len(seedS2dot):
                    for j in range(len(seedS2dot) - len(monS2dot)):
                        monS2dot.insert(0, '0')
                index = random.randint(1, len(monS2))
                childS2 = monS2[:index] + seedS2[index:]
                indexdot = random.randint(1, len(monS2dot))
                childS2dot = monS2dot[:indexdot] + seedS2dot[indexdot:]
                s2 = int("".join(map(str, childS2)), 2)
                s2dot = '0b' + ''.join(childS2dot)

                self.childMlist.append(m2+self.transformDec(m2dot))
                self.childSlist.append(s2+self.transformDec(s2dot))
            # print("交配")
    def transform(self, num):
        change = []
        a = bin(unpack('I', pack('f', num))[0])
        for x in a[2:]:
            change.append(x)
        return change

    def transformDec(self, num):
        change = float(unpack('f', pack('I', int(num, 0)))[0])
        return change
