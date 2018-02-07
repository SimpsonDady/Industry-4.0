class Data:

    '''
    a Node has three dimension,
    maxSchedule minSchedule avgSchedule,
    maybe consider the others dimension,
    like maxArrive, minArrive, avgArrive
    '''

    '''
    準排率 越靠近receivetime越好
    準達率 越靠近deadlinetime越好
    '''

    '''
    maxdelay    
    avgdelay
    '''

    def __init__(self, ID, maxSchedule, minSchedule, avgSchedule,
                 maxArrive, minArrive, avgArrive,
                 maxDelay, minDelay, avgDelay, index):
        self.ID = ID
        self.maxSchedule = maxSchedule
        self.minSchedule = minSchedule
        self.avgSchedule = avgSchedule
        self.maxArrive = maxArrive
        self.minArrive = minArrive
        self.avgArrive = avgArrive
        self.maxDelay = maxDelay
        self.minDelay = minDelay
        self.avgDelay = avgDelay
        self.index = index
        self.parent = None
        self.right = None
        self.left = None