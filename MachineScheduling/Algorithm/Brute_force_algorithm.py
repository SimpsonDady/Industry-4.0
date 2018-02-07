from Method.Data import Data
from Method.Heap import Heap
from Method.LoadData import LoadData
from Method.Skyline import Skyline
import time
import copy

class Brute_force_algorithm:

    undoneSkylineList = []
    skylinePathList = []
    candidate = []
    exchoice = []

    h = Heap()
    s = Skyline()

    edges, times, droneAll = {}, {}, {}
    node2src_d, node2src_t, dronePoint = {}, {}, {}


    machinceID, machinceCostTime, machinceRecieveTime, machinceDeadline, ID = [], [], [], [], []


    def __init__(self):
        print('Scheduling Start (Brute_force_algorithm)')

    def initialization(self, num):
        self.edges.clear(), self.times.clear(), self.droneAll.clear()
        self.node2src_d.clear(), self.node2src_t.clear(), self.dronePoint.clear()
        self.candidate.clear(), self.undoneSkylineList.clear(), self.skylinePathList.clear(), self.exchoice.clear()

        load = LoadData("1")
        self.machinceID = load.getmachinceID()
        self.machinceCostTime = load.machinceCostTime()
        self.machinceRecieveTime = load.machinceRecieveTime()
        self.machinceDeadline = load.machinceDeadline()
        self.ID = load.ID()

        for key in self.machinceID:
            self.exchoice.append(key)

    def bruteForce(self, num):
        runTime, AllrunTime = [], []
        skylineList, AllSkylineList = [], []
        originalData = []

        self.initialization(num)

#   進行資料處理(未完成)20180119
#   正規化(為完成)20180119

        for i in range(0, 10, 1):
            tmpData = Data(str(i), self.node2src_d[str(i)], self.node2src_t[str(i)], self.dronePoint[str(i)], 0)
            originalData.append(tmpData)
        # print('originalData', len(originalData))

        for length in range(4, 10, 1):
            print('bruteForce Start...')
            start = time.time()

            self.candidate = copy.deepcopy(originalData)
            skylineList = []

            # implement the bruteForce, call function
            while True:
                if len(self.candidate[0].symbol) == length:
                    break
                else:
                    tmpSymbol = self.candidate[0].symbol
                    tmpDistance = self.candidate[0].distance
                    tmpTime = self.candidate[0].time
                    tmpPoint = self.candidate[0].dronePoint

                    self.undoneSkylineList.append([tmpSymbol, tmpDistance, tmpTime, tmpPoint])
                    self.candidate = self.candidate + self.extendNode()         # add in the last of the list
                    del self.candidate[0]

            # for content in self.candidate:
            #     print(content.symbol, content.distance, content.time, content.dronePoint)

            skylineList = self.findSkylinePath()

            end = time.time()
            ti = (end - start)

            AllSkylineList.append(skylineList)

            print("time=", ti)

            runTime.append(ti)

        AllrunTime.append(runTime)

        return AllrunTime, AllSkylineList

    def findSkylinePath(self):
        skylinePath = []
        for path in self.candidate:
            flag = True  # flag == True,the data is not dominated
            for cmpPath in self.candidate:
                if path.symbol == cmpPath.symbol:
                    # print(path.symbol, cmpPath.symbol)
                    continue
                else:
                    cnt = 0
                    if path.distance > cmpPath.distance:
                        cnt += 1
                    if path.time > cmpPath.time:
                        cnt += 1
                    if path.dronePoint < cmpPath.dronePoint:
                        cnt += 1
                    if cnt == 3:
                        flag = False
                        break
            if flag:
                data = Data(path.symbol, path.distance, path.time, path.dronePoint, 0)
                skylinePath.append(data)
        return skylinePath

    def extendNode(self):
        undoneSkylineListCopy = list(self.undoneSkylineList[-1][0])
        backNode = []
        x = []
        for i in range(len(self.exchoice)):
            if self.exchoice[i][0] == undoneSkylineListCopy[-1] and \
                    self.verifyDuplication(self.undoneSkylineList[-1][0], self.exchoice[i][1]):
                x.append(self.exchoice[i][1])

        extendCandidateCopy = []
        str = ''
        for i in range(len(x)):
            extendCandidateCopy.append(self.undoneSkylineList[-1][0] + str.join(x[i]))

        for i in range(len(extendCandidateCopy)):
            length = self.extendPathDistance(extendCandidateCopy[i])
            times = self.extendPathTime(extendCandidateCopy[i])
            dronepoint = self.extendDronePoint(extendCandidateCopy[i])
            backNode.append(Data(extendCandidateCopy[i], length, times, dronepoint, 0))

        return backNode

    def verifyDuplication(self, pathCombine, expandNode):
        flag = True
        path = pathCombine
        pathList = list(path)
        #print('pathList:', pathList)
        for i in range(0, len(pathList), 1):
            if pathList[i] == expandNode:
                flag = False
        return flag

    def extendPathDistance(self, character):
        pathLength = 0
        if len(character) == 2:
            pathLength += self.undoneSkylineList[-1][1] + self.edges[character]
        else:
            pathLength += self.undoneSkylineList[-1][1] + self.edges[(character[-2] + character[-1])]

        return pathLength

    def extendPathTime(self, character):
        pathTime = 0
        if len(character) == 2:
            pathTime += self.undoneSkylineList[-1][2] + self.times[character]
        else:
            pathTime += self.undoneSkylineList[-1][2] + self.times[(character[-2] + character[-1])]
        return pathTime

    def extendDronePoint(self, character):
        dronepoint = 0
        dronepoint += self.undoneSkylineList[-1][3] + self.droneAll[character[-1]]
        return dronepoint