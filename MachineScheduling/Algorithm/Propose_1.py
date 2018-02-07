from Method.Heap import Heap
from Method.LoadData import LoadData
from Method.Data import Data
from Method.Skyline import Skyline
from Method.Math.Math import Math
import time

class Algorithm:

    h = Heap()
    s = Skyline()
    m = Math()

    machineID, machineCostTime, machineReceiveTime, machineDeadline, ID = [], [], [], [], []
    undoneSkyline, skylinePathList, expand = [], [], []
    data = {}
    sPoint = "NULL"

    systemTime = '2017-12-3.14:12:30'

    def __init__(self):
        print('Scheduling Start!!!')

    def initialization(self, num):
        load = LoadData("1")
        self.machineID = load.getmachinceID()
        self.machineCostTime = load.getmachinceCostTime()
        self.machineReceiveTime = load.getmachinceRecieveTime()
        self.machineDeadline = load.getmachinceDeadline()
        self.ID = load.getID()

        for key in self.ID:
            self.expand.append(key)

    def DHSQA(self, num):
        runTime, AllrunTime = [], []                                            # Record those we want to know
        AllSkylineList = []

        self.initialization(num)
        # self.sPoint = self.findInitialPoint()

        for length in range(4, 5, 1):                                         # set the how many node we wnat to find
            start = time.time()                                                 # calcaulate the run time(start)
            skylineList = []                                                    # To store the found those skylines

            originalPoint = {}
            # bug?

            skylineList.clear()
            if not skylineList:
                flag = False
            else:
                flag = True

            print('\n---the First Step---')
            while (not flag):

                originalPoint = self.findSkylinePath(originalPoint)             # first skyline query
                tmpSymbol = originalPoint[1].ID                           # the first node of the heapMin that the value is minimun
                maxValue = originalPoint[1].maxSchedule
                minValue = originalPoint[1].minSchedule
                avgValue = originalPoint[1].avgSchedule
                maxArrive = originalPoint[1].maxArrive
                minArrive = originalPoint[1].minArrive
                avgArrive = originalPoint[1].avgArrive
                maxDelay = originalPoint[1].maxDelay
                minDelay = originalPoint[1].minDelay
                avgDelay = originalPoint[1].avgDelay


                for i in range(1, len(originalPoint) + 1, 1):                   # print those skyline candidation
                    if len(tmpSymbol.split("->")) >= length:                                # judgning those full skyline candidation
                        skylineList.append(Data(tmpSymbol, maxValue, minValue, avgValue,
                                                maxArrive, minArrive, avgArrive, maxDelay, minDelay, avgDelay, 0))
                        flag = True
                        print('\nExtend successful and add to SkylineList = ', originalPoint[i].ID)
                        print('-----------------------------------------------------')
                        print('skyline are = ', skylineList[0].ID)
                        print('-----------------------------------------------------')
                        # print('These remain are =')
                        break
                    # print(originalPoint[i].ID)
                    # print("ID:", originalPoint[i].ID, "\n")
                    # print("max", originalPoint[i].maxSchedule)
                    # print("min", originalPoint[i].minSchedule)
                    # print("avg", originalPoint[i].avgSchedule)
                    # print("total", originalPoint[i].maxSchedule + originalPoint[i].minSchedule + originalPoint[i].avgSchedule)
                    # print("------------------------------------")

            originalPoint = self.h.getMaxHeapNode(originalPoint)

            print('\n---the Second Step---')
            skylineList, originalPoint = self.SPGA(skylineList, originalPoint, length)

            while (len(originalPoint) > 0):
                skylineList, originalPoint = self.SPGA(skylineList, originalPoint, length)

            # for i in range(len(skylineList)):  # Output the skylineList
            #     print('skyline are = ', skylineList[i].symbol, skylineList[i].distance,
            #           skylineList[i].time, skylineList[i].dronePoint, 'and ')
            #     print('-----------------------------------------------------')

            end = time.time()
            ti = (end - start)

            AllSkylineList.append(skylineList)
            runTime.append(ti)
        AllrunTime.append(runTime)
        return AllrunTime, AllSkylineList

    def findInitialPoint(self):
        point = {}
        for i in range(0, len(self.machineReceiveTime), 1):
            for j in range(i + 1, len(self.machineReceiveTime), 1):
                t1 = self.splitTime(self.machineDeadline[i])
                t2 = self.splitTime(self.machineDeadline[j])
                diff = []
                for k in range(0, len(t1), 1):
                    tmp = t1[k] - t2[k]
                    if tmp < 0:
                        tmp = tmp * (-1)
                    diff.append(tmp)
                point[self.ID[i] + " " + self.ID[j]] = self.calculateTime(diff)
        startPoint = sorted(point, key=lambda x: point[x])[0]
        return startPoint

    def splitTime(self, string):
        dataTime = []
        tmp = string.split(".")
        dataOfDate = tmp[0]
        dataOfTime = tmp[1]
        tmp = dataOfDate.split("-")
        for i in range(0, len(tmp), 1):
            dataTime.append(int(tmp[i]))
        tmp = dataOfTime.split(":")
        for i in range(0, len(tmp), 1):
            dataTime.append(int(tmp[i]))
        return dataTime

    def calculateTime(self, data):
        sum = 0
        sum = sum + (31556926 * data[0])
        sum = sum + (2629743 * data[1])
        sum = sum + (86400 * data[2])
        sum = sum + (3600 * data[3])
        sum = sum + (60 * data[4])
        sum = sum + data[5]
        return sum

    def findSkylinePath(self, data):
        precisionOfScheduling, precisionOfArriving, tmpDelay, tmpDelayList, precisionOfDelay = [], [], [], [], []
        inputOfSchedule, inputOfArrive, inputOfDelay = [], [], []
        dTime = self.splitTime(self.systemTime)
        modifiedData = data
        if not data:
            # Create Heaptree
            spoint = self.expand
            for i in range(0, len(spoint), 1):
                tmpDelay = []
                receive = self.splitTime(self.machineReceiveTime[int(spoint[i])])
                deadline = self.splitTime(self.machineDeadline[int(spoint[i])])
                diff, diff2 = [], []
                for j in range(0, 6, 1):
                    tmp = deadline[j] - receive[j]              # deadtime to receive
                    tmp2 = deadline[j] - int(dTime[j])          # deadtime minus systemTime
                    diff.append(tmp)
                    diff2.append(tmp2)
                deadToReceive = self.calculateTime(diff)
                deadToSystem = self.calculateTime(diff2)
                begin = deadToReceive
                finished = 3600 * int(self.machineCostTime[int(spoint[i])])
                delay = deadToSystem
                precisionOfScheduling.append((begin / deadToReceive) + 1)
                precisionOfArriving.append((finished / deadToReceive) + 1)
                tmpDelay.append(delay)

                sumOfSchedule, sumOfArrive = 0.0, 0.0
                for j in range(0, len(precisionOfScheduling), 1):
                    sumOfSchedule = sumOfSchedule + precisionOfScheduling[j]
                    sumOfArrive = sumOfArrive + precisionOfArriving[j]

                maxSchedule = max(precisionOfScheduling)
                minSchedule = min(precisionOfScheduling)
                avgSchedule = sumOfSchedule / len(precisionOfScheduling)

                maxArrive = max(precisionOfArriving)
                minArrive = min(precisionOfArriving)
                avgArrive = sumOfArrive / len(precisionOfArriving)

                inputOfSchedule.append([maxSchedule, minSchedule, avgSchedule])
                inputOfArrive.append([maxArrive, minArrive, avgArrive])
                tmpDelayList.append(tmpDelay)

            maxDelayValue = tmpDelayList[0][0]
            minDelayValue = tmpDelayList[0][0]
            for i in range(0, len(tmpDelayList), 1):
                if max(tmpDelayList[i]) >= maxDelayValue:
                    maxDelayValue = max(tmpDelayList[i])
                if min(tmpDelayList[i]) <= minDelayValue:
                    minDelayValue = min(tmpDelayList[i])

            tmpList = []
            for i in range(0, len(tmpDelayList), 1):
                for j in range(0, len(tmpDelayList[i]), 1):
                    tmpList.append(self.m.Normalization(tmpDelayList[i][j], maxDelayValue, minDelayValue))
                    if len(tmpList) == len(tmpDelayList[i]):
                        precisionOfDelay.append(tmpList)

            sumOfDelay= 0.0
            for i in range(0, len(precisionOfDelay), 1):
                for j in range(0, len(precisionOfDelay[i]), 1):
                    sumOfDelay = sumOfDelay + precisionOfDelay[i][j]
                    maxDelay = max(precisionOfDelay[i])
                    minDelay = min(precisionOfDelay[i])
                    avgDelay = sumOfDelay / len(precisionOfDelay[i])
                    inputOfDelay.append([maxDelay, minDelay, avgDelay])

            for i in range(0, len(spoint), 1):
                ID = spoint[i]
                maxSchedule = inputOfSchedule[i][0]
                minSchedule = inputOfSchedule[i][1]
                avgSchedule = inputOfSchedule[i][2]
                maxArrive = inputOfArrive[i][0]
                minArrive = inputOfArrive[i][1]
                avgArrive = inputOfArrive[i][2]
                maxDelay = inputOfDelay[i][0]
                minDelay = inputOfDelay[i][1]
                avgDelay = inputOfDelay[i][2]
                modifiedData = self.h.insertNode(modifiedData, ID,
                                                 maxSchedule, minSchedule, avgSchedule,
                                                 maxArrive, minArrive, avgArrive,
                                                 maxDelay, minDelay, avgDelay)
        symbol = modifiedData[1].ID
        # print('\nWe will extend', symbol)
        maxSchedule, minSchedule, avgSchedule, \
        maxArrive, minArrive, avgArrive, maxDelay, minDelay, avgDelay = self.getDimOfData(modifiedData)        #set the value not set the address
        self.undoneSkyline.append([symbol, maxSchedule, minSchedule, avgSchedule,
                                   maxArrive, minArrive, avgArrive, maxDelay, minDelay, avgDelay])

        modifiedData = self.h.getMaxHeapNode(modifiedData)
        modifiedData = self.extendNode(modifiedData)
        return modifiedData

    def getDimOfData(self, data):
        tmpMaxSchedule = data[1].maxSchedule
        tmpMinSchedule = data[1].minSchedule
        tmpAvgSchedule = data[1].avgSchedule
        tmpMaxArrive = data[1].maxArrive
        tmpMinArrive = data[1].minArrive
        tmpAvgArrive = data[1].avgArrive
        tmpMaxDelay = data[1].maxDelay
        tmpMinDelay = data[1].minDelay
        tmpAvgDelay = data[1].avgDelay
        return tmpMaxSchedule, tmpMinSchedule, tmpAvgSchedule,\
               tmpMaxArrive, tmpMinArrive, tmpAvgArrive, tmpMaxDelay, tmpMinDelay, tmpAvgDelay

    def SPGA(self, skyline, data, length):                                   # Second,compare the first skyline and the ramain path
        modifiedData = {}
        modifiedData = data
        if len(modifiedData) > 0:
            tmpSymbol = modifiedData[1].ID
            maxSchedule, minSchedule, avgSchedule,\
            maxArrive, minArrive, avgArrive, maxDelay, minDelay, avgDelay = self.getDimOfData(modifiedData)
            # print('\nWe will compare ', tmpSymbol)
            temp = Data(tmpSymbol, maxSchedule, minSchedule, avgSchedule,
                        maxArrive, minArrive, avgArrive, maxDelay, minDelay, avgDelay, 0)
            if self.s.skylineAlogrithm(temp, skyline):                                     #temp is not dominated by skylineList
                if len(temp.ID.split("->")) >= length:                                             #judgning those full skyline candidation
                    # print('\nWe will append to skylineList ', temp.ID)
                    skyline.append(temp)
                    modifiedData = self.h.getMaxHeapNode(modifiedData)
                else:
                    # print('\nWe will extend ', temp.ID)
                    self.undoneSkyline.append([tmpSymbol, maxSchedule, minSchedule, avgSchedule,
                                               maxArrive, minArrive, avgArrive, maxDelay, minDelay, avgDelay])
                    modifiedData = self.h.getMaxHeapNode(modifiedData)
                    modifiedData = self.extendNode(modifiedData)
            else:                                                                               #temp is dominated
                # print(temp.ID, ' is worse and we don\'t extend = ')
                modifiedData = self.h.getMaxHeapNode(modifiedData)
        return skyline, modifiedData

    def extendNode(self, data):                                                                       #extend the minheap tree
        undoneSkylineCopy = self.undoneSkyline[-1][0].split("->")
        willExpand = []
        modifiedData = data
        dTime = self.splitTime(self.systemTime)
        for i in range(len(self.expand)):
            if self.expand[i] != undoneSkylineCopy[-1] and \
                    self.verifyDuplication(self.undoneSkyline[-1][0].split("->"), self.expand[i]):
                willExpand.append(self.expand[i])
        extendScheduleCopy = []
        str = ''
        for i in range(len(willExpand)):
            extendScheduleCopy.append(self.undoneSkyline[-1][0] + "->" +str.join(willExpand[i]))          #extend the node(A->AB)

        inputOfSchedule, inputOfArrive, inputOfDelay = [], [], []

        for i in range(len(extendScheduleCopy)):
            precisionOfScheduling, precisionOfArriving, tmpDelay, tmpDelayList, precisionOfDelay = [], [], [], [], []
            tmpID = extendScheduleCopy[i].split("->")
            for j in range(0, len(tmpID), 1):
                tmpDelay = []
                receive = self.splitTime(self.machineReceiveTime[int(tmpID[j])])
                deadline = self.splitTime(self.machineDeadline[int(tmpID[j])])
                diff, diff2 = [], []
                for k in range(0, 6, 1):
                    tmp = deadline[k] - receive[k]              # deadtime to receive
                    tmp2 = deadline[k] - int(dTime[k])        # deadtime minus systemTime
                    diff.append(tmp)
                    diff2.append(tmp2)
                deadToReceive = self.calculateTime(diff)
                deadToSystem = self.calculateTime(diff2)
                begin = deadToReceive
                finished = 3600 * int(self.machineCostTime[int(tmpID[0])])
                delay = deadToSystem
                for l in range(0, j, 1):
                    begin = deadToReceive - 3600 * int(self.machineCostTime[int(tmpID[l])])
                    delay = delay - 3600 * int(self.machineCostTime[int(tmpID[l])])
                for l in range(1, j + 1, 1):
                    finished = finished + 3600 * int(self.machineCostTime[int(tmpID[l])])
                precisionOfScheduling.append((begin / deadToReceive) + 1)
                precisionOfArriving.append((finished / deadToReceive) + 1)
                tmpDelay.append(delay)

                sumOfSchedule, sumOfArrive = 0.0, 0.0
                for l in range(0, len(precisionOfScheduling), 1):
                    sumOfSchedule = sumOfSchedule + precisionOfScheduling[l]
                    sumOfArrive = sumOfArrive + precisionOfArriving[l]
                maxSchedule = max(precisionOfScheduling)
                minSchedule = min(precisionOfScheduling)
                avgSchedule = sumOfSchedule / len(precisionOfScheduling)

                maxArrive = max(precisionOfArriving)
                minArrive = min(precisionOfArriving)
                avgArrive = sumOfArrive / len(precisionOfArriving)

                inputOfSchedule.append([maxSchedule, minSchedule, avgSchedule])
                inputOfArrive.append([maxArrive, minArrive, avgArrive])
                tmpDelayList.append(tmpDelay)

            maxDelayValue, minDelayValue = tmpDelayList[0][0], tmpDelayList[0][0]
            for j in range(0, len(tmpDelayList), 1):
                if max(tmpDelayList[j]) >= maxDelayValue:
                    maxDelayValue = max(tmpDelayList[j])
                if min(tmpDelayList[j]) <= minDelayValue:
                    minDelayValue = min(tmpDelayList[j])

            tmpList = []
            for j in range(0, len(tmpDelayList), 1):
                for k in range(0, len(tmpDelayList[j]), 1):
                    tmpList.append(self.m.Normalization(tmpDelayList[j][k], maxDelayValue, minDelayValue))
                    if len(tmpList) == len(tmpDelayList[j]):
                        precisionOfDelay.append(tmpList)

            sumOfDelay = 0.0
            for j in range(0, len(precisionOfDelay), 1):
                for k in range(0, len(precisionOfDelay[j]), 1):
                    sumOfDelay = sumOfDelay + precisionOfDelay[j][k]
                    maxDelay = max(precisionOfDelay[j])
                    minDelay = min(precisionOfDelay[j])
                    avgDelay = sumOfDelay / len(precisionOfDelay[j])
                    inputOfDelay.append([maxDelay, minDelay, avgDelay])
        #
        # print(extendScheduleCopy)
        # print("a", inputOfSchedule, len(inputOfSchedule))
        # print("b", inputOfArrive, len(inputOfArrive))
        # print("c", inputOfDelay, len(inputOfDelay))
        for i in range(0, len(extendScheduleCopy), 1):
            maxSchedule = inputOfSchedule[i][0]
            minSchedule = inputOfSchedule[i][1]
            avgSchedule = inputOfSchedule[i][2]
            maxArrive = inputOfArrive[i][0]
            minArrive = inputOfArrive[i][1]
            avgArrive = inputOfArrive[i][2]
            maxDelay = inputOfDelay[i][0]
            minDelay = inputOfDelay[i][1]
            avgDelay = inputOfDelay[i][2]
            modifiedData = self.h.insertNode(modifiedData, extendScheduleCopy[i],
                                             maxSchedule, minSchedule, avgSchedule,
                                             maxArrive, minArrive, avgArrive,
                                             maxDelay, minDelay, avgDelay)
        return modifiedData

    def verifyDuplication(self, scheduleCombine, expandSchedule):
        flag = True                                                                             # True : no duplicate, Flase : duplicate
        secheduleList = list(scheduleCombine)
        for i in range(0, len(secheduleList), 1):
            if secheduleList[i] == expandSchedule:
                flag = False
        return flag

    def showTree(self, data):
        for i in range(1, len(data) + 1, 1):
            print("ID:", data[i].ID, "\n")
            print("max", data[i].maxSchedule)
            print("min", data[i].minSchedule)
            print("avg", data[i].avgSchedule)
            print("total", data[i].maxSchedule + data[i].minSchedule + data[i].avgSchedule)
            print("------------------------------------")