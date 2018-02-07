import random
import math

class Math:
    def coorelate(self, data):
        # print('正相關')
        data = data / 100
        return data + math.exp((data ** 1.5) / 0.5) * (random.uniform(0, 1) * 0.8 - 0.4)

    def anti_coorelate(self, data):
        # print('負相關')
        data = data / 100
        return (-data + math.exp((-data ** 1.5) / 0.5) * (random.uniform(0, 1) * 0.8 - 0.4))

    def independent(self,data):
        # print('獨立性')
        return random.uniform(-1, 1)

        # x 資料正規化

    def Normalization(self, xinput, interval):
        xinput = float(xinput)
        if (len(interval)) <= 1:
            output = 0.0
        elif (max(interval) - min(interval)) == 0:
            output = 0.0
        else:
            output = 2 * (xinput - min(interval)) / (max(interval) - min(interval))
        return output

    #Overloding
    def Normalization(self, xinput, maxValue, minValue):
        xinput = float(xinput)
        if maxValue - minValue == 0:
            output = 0.0
        else:
            output = 2 * (xinput - maxValue) / (maxValue - minValue)
        return output

    # y 資料反正規化
    def inverseNormalization(self, yinput, interval=[]):
        return ((yinput + 1) / 2) * (max(interval) - min(interval)) + min(interval)

