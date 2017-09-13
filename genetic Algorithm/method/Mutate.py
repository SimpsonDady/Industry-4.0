import random

from struct import unpack, pack


class Mutate:
    def __init__(self, mdata, sdata, filter):
        self.mdata = mdata
        self.sdata = sdata
        self.filter = filter
        self.kid = {}
        self.mutate()

    def mutate(self):
        for i in self.mdata:
            if random.randint(1, 100) <= 20:
                mutate_index = random.randrange(len(i))
                if i[mutate_index] == '0':
                    i[mutate_index] = '1'
                else:
                    i[mutate_index] = '0'
        for j in self.sdata:
            if random.randint(1, 100) <= 20:
                mutate_index = random.randrange(len(j))
                if j[mutate_index] == '0':
                    j[mutate_index] = '1'
                else:
                    j[mutate_index] = '0'
        print("突變")
        if self.filter:
            count = 0
            num = 1
            flo = []
            for k in range(400):
                m = '0b' + ''.join(self.mdata[k])
                flo.append(self.transform(m))
                s = '0b' + ''.join(self.sdata[k])
                flo.append(self.transform(s))
                count += 1
                if count == 2:
                    self.kid.update({"child" + str(num): flo})
                    flo = []
                    count = 0
                    num += 1
        else:
            flo = []
            for l in range(200):
                m = '0b' + ''.join(self.mdata[l])
                flo.append(self.transform(m))
                s = '0b' + ''.join(self.sdata[l])
                flo.append(self.transform(s))
                self.kid.update({"child" + str(l+1): flo})
                flo = []

    def transform(self, num):
        change = float(unpack('f', pack('I', int(num, 0)))[0])
        return change
