from math import pi, e, sqrt


class Fitness:
    def __init__(self, kid, data, monlist,filter):
        self.kid = kid
        self.data = data
        self.filter = filter
        self.stop = False
        self.mon = []
        self.monlist = monlist
        self.fitness()

    def fitness(self):
        result = []
        geneavage = {}
        for key, value in self.kid.items():
            for j in self.data:
                gauss = 1 / (sqrt(2 * pi) * value[1]) * e ** (-0.5 * (float(j - value[0]) / value[1]) ** 2)
                if self.filter:
                    gauss2 = 1 / (sqrt(2 * pi) * value[3]) * e ** (-0.5 * (float(j - (value[0] + value[2])) / value[3]) ** 2)
                    gauss3 = 1 / (sqrt(2 * pi) * value[3]) * e ** (-0.5 * (float(j - (value[0] + (2 * value[2]))) / value[3]) ** 2)
                    gauss4 = 1 / (sqrt(2 * pi) * value[3]) * e ** (-0.5 * (float(j - (value[0] + (3 * value[2]))) / value[3]) ** 2)
                    result.append((gauss+gauss2+gauss3+gauss4))
                else:
                    result.append(gauss)
            geneavage.update({key: sum(result) / len(result)})  # 基因適應的平均
            result = []
        # print(geneavage)
        print("...............")
        # while max(geneavage.values()) > 1:
        #     print("..............",max(geneavage.values()))
        #     for key, value in geneavage.items():
        #         if value == max(geneavage.values()):
        #             geneavage.pop(key)
        #             break
        for key, value in geneavage.items():
            if 0.9 <= value <= 1:
                self.stop = True
                print("find")
            if value == max(geneavage.values()):
                self.mon = self.kid[key]
        self.monlist.append(self.mon)
        print("bestmon     ",self.mon)
        print(max(geneavage.values()))
