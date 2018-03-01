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
                dec = list(bin(int(i))[2:])
                dot = self.transformbin(i-int(i))
                mutate_index = random.randrange(len(dec))
                dot_index = random.randrange(len(dot))
                if dec[mutate_index] == '0':
                    dec[mutate_index] = '1'
                else:
                    dec[mutate_index] = '0'
                if dot[dot_index] == '0':
                    dot[dot_index] = '1'
                else:
                    dot[dot_index] = '0'
                i = int("".join(map(str, dec)), 2) + self.transform('0b' + ''.join(dot))

        for j in self.sdata:
            if random.randint(1, 100) <= 20:
                dec = list(bin(int(j))[2:])
                dot = self.transformbin(j - int(j))
                mutate_index = random.randrange(len(dec))
                dot_index = random.randrange(len(dot))
                if dec[mutate_index] == '0':
                    dec[mutate_index] = '1'
                else:
                    dec[mutate_index] = '0'
                if dot[dot_index] == '0':
                    dot[dot_index] = '1'
                else:
                    dot[dot_index] = '0'
                j = int("".join(map(str, dec)), 2) + self.transform('0b' + ''.join(dot))
        # print("突變")
        if self.filter:
            count = 0
            num = 1
            flo = []
            for k in range(1600):
                flo.append(self.mdata[k])
                if self.sdata[k] == 0.0:
                    flo.append(0.0000000000000001)
                else:
                    flo.append(self.sdata[k])
                count += 1
                if count == 2:
                    self.kid.update({"child" + str(num): flo})
                    flo = []
                    count = 0
                    num += 1
        else:
            flo = []
            for l in range(800):
                flo.append(self.mdata[l])
                if self.sdata[l] == 0.0:
                    flo.append(0.0000000000000001)
                else:
                    flo.append(self.sdata[l])
                self.kid.update({"child" + str(l+1): flo})
                flo = []
        # print(self.kid)

    def transform(self, num):
        change = float(unpack('f', pack('I', int(num, 0)))[0])
        return change

    def transformbin(self, num):
        change = []
        a = bin(unpack('I', pack('f', num))[0])
        for x in a[2:]:
            change.append(x)
        return change
