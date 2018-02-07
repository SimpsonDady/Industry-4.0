from Method.Data import Data
from Method.Math.Math import Math

class Heap:

    m = Math()

    root = None
    cnt = 0
    heapTree = {}

    def initialization(self):
        print('Create a heap Tree......')

    def __heapSort(self):
        innerNode = int(len(self.heapTree) / 2)
        for i in range(innerNode, 0, -1):
            self.__heapify(self.heapTree, i, len(self.heapTree))

    def __heapify(self, data, root, length):
        leftChild = 2 * root
        rightChild = 2 * root + 1
        maxNode = -1

        if leftChild < length and self.calWeigthPoint(data[leftChild]) > self.calWeigthPoint(data[root]):
            maxNode = leftChild
        else:
            maxNode = root

        if rightChild < length and self.calWeigthPoint(data[rightChild]) > self.calWeigthPoint(data[maxNode]):
            maxNode = rightChild

        if(maxNode != root):
            self.__swap(data, root, maxNode)
            self.__heapify(data, maxNode, length)

    def __swap(self, data, x, y):
        tmp = data[x].ID
        data[x].ID = data[y].ID
        data[y].ID = tmp

        tmp = data[x].maxSchedule
        data[x].maxSchedule = data[y].maxSchedule
        data[y].maxSchedule = tmp

        tmp = data[x].minSchedule
        data[x].minSchedule = data[y].minSchedule
        data[y].minSchedule = tmp

        tmp = data[x].avgSchedule
        data[x].avgSchedule = data[y].avgSchedule
        data[y].avgSchedule = tmp

        tmp = data[x].maxArrive
        data[x].maxArrive = data[y].maxArrive
        data[y].maxArrive = tmp

        tmp = data[x].minArrive
        data[x].minArrive = data[y].minArrive
        data[y].minArrive = tmp

        tmp = data[x].avgArrive
        data[x].avgArrive = data[y].avgArrive
        data[y].avgArrive = tmp

        tmp = data[x].maxDelay
        data[x].maxDelay = data[y].maxDelay
        data[y].maxDelay = tmp

        tmp = data[x].minDelay
        data[x].minDelay = data[y].minDelay
        data[y].minDelay = tmp

        tmp = data[x].avgDelay
        data[x].avgDelay = data[y].avgDelay
        data[y].avgDelay = tmp

    def insertNode(self, data, symbol, maxSchedule, minSchedule, avgSchedule,
                   maxArrive, minArrive, avgArrive,
                   maxDelay, minDelay, avgDelay):                   #Insert some Node into Heap Tree
        index = len(data) + 1
        if index > 1:
            parentIndex = int(index / 2)
            newNode = Data(symbol, maxSchedule, minSchedule, avgSchedule,
                           maxArrive, minArrive, avgArrive,
                           maxDelay, minDelay, avgDelay, index)
            data[index] = newNode
            if newNode.index == 2 * (data[parentIndex].index):
                data[parentIndex].left = newNode
            else:
                data[parentIndex].right = newNode
            newNode.parent = data[parentIndex]                                                   #set newnode.parent

            flag = False                                                                         #heapify the lastest nodes
            while(flag != True):
                if self.calWeigthPoint(data[index]) > self.calWeigthPoint(data[parentIndex]):
                    self.__swap(data, index, parentIndex)
                    index = parentIndex
                    parentIndex = int(parentIndex / 2)
                    if parentIndex == 0:
                        break
                else:
                    flag = True
        else:
            newNode = Data(symbol, maxSchedule, minSchedule, avgSchedule,
                           maxArrive, minArrive, avgArrive,
                            maxDelay, minDelay, avgDelay, index)
            data[index] = newNode                                                            #how many heapTree do we use
        return data                                                                 #return the modified maxheap tree

    def getMaxHeapNode(self, data):
        index = len(data)
        self.__swap(data, 1, index)
        del data[index]                                                             #delete the lastest node
        self.__heapify(data, 1, len(data))                                          #heap the tree to conform the maxheap standard
        return data                                                                 #return the elem and the modify maxHeap tree

    def calWeigthPoint(self, data):                                                 #calcilate the weight,(rangesValue=TreeDict) bug?
        # # get the max
        allPoint = data.minSchedule + data.avgSchedule\
                   + data.maxArrive + data.avgArrive + data.avgDelay
        return allPoint

    def getTreeDictionary(self):
        return self.heapTree
