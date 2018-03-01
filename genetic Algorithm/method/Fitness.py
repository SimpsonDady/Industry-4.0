from math import pi, e, sqrt

import math
from time import sleep

import numpy as np
import winsound


class Fitness:
    def __init__(self, kid, data, monlist, filter, round):
        self.kid = kid
        self.data = data
        self.filter = filter
        self.stop = False
        self.mon = []
        self.monlist = monlist
        self.endans = []
        self.endanslist = []
        self.round = round
        self.fitness()

    def fitness(self):
        result = []
        geneavage = {}
        c = 1
        for key, value in self.kid.items():
            # print(value, "v")
            whichlist = []
            for j in self.data:
                gausslist = []
                gauss = np.exp(-((j - value[0])**2)/(2*value[1]**2)) / (value[1] * np.sqrt(2*np.pi)) # gauss 常態分布分數
                # gauss = 1 / (sqrt(2 * pi) * value[1]) * e ** (-0.5 * (float(j - value[0]) / value[1]) ** 2)
                gausslist.append(gauss)
                if self.filter:  # 判別資料跑做兩件還是一件
                    for i in range(1, 10):
                        multiplegauss = np.exp(-((j - (value[0] + (i * value[2])))**2)/(2*value[3]**2)) / (value[3] * np.sqrt(2*np.pi))  # gauss 常態分布分數
                        # multiplegauss = 1 / (sqrt(2 * pi) * value[3]) * e ** (-0.5 * (float(j - (value[0] + (i * value[2]))) / value[3]) ** 2)
                        gausslist.append(multiplegauss)
                    which = gausslist.index(max(gausslist))+1
                    whichlist.append(which)
                    # print(which)
                    # print(gausslist)
                    if value[0] > value[2]:
                        if (max(gausslist)/which) * value[2] == 0:
                            ans = 0.0
                        else:
                            if (value[0] - value[2]) == 0:
                                c = 1
                            elif value[0] / (value[0] - value[2]) > (value[0] - value[2]) / value[0]:
                                c = value[0] / (value[0] - value[2])
                            else:
                                c = (value[0] - value[2]) / value[0]
                            ans = ((max(gausslist)/which) * value[2] / value[0]) / c
                    else:
                        # if (max(gausslist)/which) * value[0] == 0:
                        #     ans = 0.0
                        # else:
                        #     if (value[0] - value[2]) == 0:
                        #         c = 1
                        #     elif value[0] / (value[0] - value[2]) > (value[0] - value[2]) / value[0]:
                        #         c = value[0] / (value[0] - value[2])
                        #     else:
                        #         c = (value[0] - value[2]) / value[0]
                        ans = ((max(gausslist)/which) * value[0] / value[2]) / c
                    if math.isnan(max(gausslist)):
                        ans = 0.0
                        # print(True)
                    result.append((ans))
                    # print(ans,"ans")
                else:
                    if math.isnan(gauss):
                        gauss = 0.0
                        # print(True)
                    result.append(gauss)
            # print(result)
            if math.isnan(sum(result) / len(result)):
                geneavage.update({key: 0.0})
            else:
                # print(key, result, "result")
                # print(whichlist)
                if whichlist == []:
                    geneavage.update({key: sum(result) / len(result)})
                else:
                    geneavage.update({key: sum(result) / len(result)*min(result)}) #  基因適應的平均 *min(result)*whichlist[result.index(min(result))]
                    # print(sum(result) / len(result), "result")
                    # print(sum(result) / len(result) * min(result))
            result = []
        # print(geneavage)
        # print("...............")
        # while max(geneavage.values()) > 1:
        #     print("..............",max(geneavage.values()))
        #     for key, value in geneavage.items():
        #         if value == max(geneavage.values()):
        #             geneavage.pop(key)
        #             break
        for key, value in geneavage.items():
            # if value > 10:
            #     print(key)
            #     self.play_music()
            #     sleep(1)
            if 0.9 <= value <= 1:
                self.stop = True
                # if self.kid[key][0]>9:
                #     self.play_music()
                #     sleep(1)
                self.endans = self.kid[key]
                self.endans.append(value)
                self.endanslist.append(self.endans)
                print("find")
            # else:
            #     self.endans = self.kid[key]
            #     self.endans.append(value)
            #     self.endanslist.append(self.endans)
            #     if self.round == 100:
            #         self.stop = True
            # if value == max(geneavage.values()):
                self.mon = self.kid[key]
                self.mon.append(value)
        self.monlist.append(self.mon)
        print("bestmon     ", self.mon)
        # print(self.monlist)
        # sleep(1)
        print(max(geneavage.values()))
    def play_music(self):
        winsound.PlaySound('alert', winsound.SND_ASYNC)