class Filter:
    def __init__(self,data):
        self.data = data
        self.outdata = []
        self.multiple = False
        self.filter()
    def filter(self):
        less_zero = []
        large_zero = []
        zero = False
        for i in self.data:
            if i < 1:
                zero = True
                break
        if zero:
            for j in self.data:
                if j < 1:
                    less_zero.append(j)
                else:
                    large_zero.append(j)
            if sum(large_zero)/len(large_zero) > sum(less_zero)/len(less_zero)*2:
                self.outdata = large_zero
            else:
                self.outdata = self.data
        else:
            self.outdata = self.data

        avage = sum(self.outdata)/len(self.outdata)
        # print(self.outdata)
        for k in self.outdata:
            if avage-k > 1.5 or k - avage > 1.5:
                self.multiple = True
                break
            else:
                self.multiple = False
        # print(self.multiple)
