class Skyline:

    '''
    True, the data is not dominated
    False, the data is dominated
    '''

    def skylineAlogrithm(self, data, skylineList):
        # print('skyline Comparsion')
        flag = True                                                   # flag == True,the data is not dominated
        length = len(skylineList)
        for i in range(length):
            cnt = 0
            cnt1 = 0
            # if data.maxSchedule > skylineList[i].maxSchedule:
            #     cnt += 1
            if data.minSchedule <= skylineList[i].minSchedule:
                cnt += 1
                if data.minSchedule == skylineList[i].minSchedule:
                    cnt1 = cnt1 + 1
            if data.avgSchedule <= skylineList[i].avgSchedule:
                cnt += 1
                if data.avgSchedule == skylineList[i].avgSchedule:
                    cnt1 += 1
            if data.maxArrive <= skylineList[i].maxArrive:
                cnt += 1
                if data.maxArrive == skylineList[i].maxArrive:
                    cnt1 = cnt1 + 1
            # if data.minArrive <= skylineList[i].minArrive:
            #     cnt += 1
            #     if data.minArrive == skylineList[i].minArrive:
            #         cnt1 += 1
            if data.avgArrive <= skylineList[i].avgArrive:
                cnt += 1
                if data.avgArrive == skylineList[i].avgArrive:
                    cnt1 = cnt1 + 1

            if data.minDelay >= skylineList[i].minDelay:
                cnt += 1
                if data.minDelay == skylineList[i].minDelay:
                    cnt1 = cnt1 + 1

            if data.avgDelay >= skylineList[i].avgDelay:
                cnt += 1
                if data.avgDelay == skylineList[i].avgDelay:
                    cnt1 = cnt1 + 1

            if cnt == 6 and cnt1 != 6:
                flag = False
                break
        return flag