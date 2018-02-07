from Method.Math.Math import Math

class LoadData:

    '''

    machinceID String
    machinceCostTime INT
    machinceRecieveTime String
    machinceDeadline String
    ID String

    '''

    machinceID = []
    machinceCostTime = []
    machinceRecieveTime = []
    machinceDeadline = []
    ID = []

    m = Math()

    def __init__(self, num):
        print('Load Data......')
        self.num = num
        self.loadData(self.num)

    def loadData(self, num):
        tmp = []
        tmpDetail = []

        # For Windows
        f = open('D:/pythonScript/MachineScheduling/Data/MachinceData/data'+num+'.txt', 'r', encoding='UTF-8')

        # For MAC
        # f = open('/Users/yurenchen/Desktop/MachineScheduling/Data/MachinceData/data' + num + '.txt', 'r', encoding='UTF-8')
        while True:
            d = f.readline()
            if d == '':
                break
            tmp.append(d)
        for i in range(len(tmp)):
            tmpDetail.append(tmp[i].split(";"))
            '''
            tmpDetail[i][0], 機台編號
            tmpDetail[i][1], 預估花費時間
            tmpDetail[i][2], 訂單接收時間
            tmpDetail[i][3], 訂單最終期限時間
            tmpDetail[i][4], 機台代號(自訂)
            '''
            self.machinceID.append(tmpDetail[i][0])
            self.machinceCostTime.append(tmpDetail[i][1])
            self.machinceRecieveTime.append(tmpDetail[i][2])
            self.machinceDeadline.append(tmpDetail[i][3])
            self.ID.append(tmpDetail[i][4].split("\n")[0])
        f.close()

    def getmachinceID(self):
        return self.machinceID

    def getmachinceCostTime(self):
        return self.machinceCostTime

    def getmachinceRecieveTime(self):
        return self.machinceRecieveTime

    def getmachinceDeadline(self):
        return self.machinceDeadline

    def getID(self):
        return self.ID