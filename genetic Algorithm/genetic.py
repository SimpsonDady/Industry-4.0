import time

from openpyxl import Workbook

from method.CreateChlid import CreateChild
from method.Crossover import Crossover
from method.Filter import Filter
from method.Fitness import Fitness
from method.Mutate import Mutate
from method.ReadFile import ReadFile

ws = Workbook()
wb = ws.active
wb.append(['工具代碼', '一件時間','','兩件時間'])
readfile = ReadFile()
anslist = {}
for time in range(10):
    ans = {}
    for key, value in readfile.information.items():
        print(key)
        filter = Filter(value)
        data = filter.outdata
        print(data)
        stop = True
        remend = []
        monlist = []
        round = 1
        while stop:
            create_child = CreateChild(filter.multiple)
            fitness = Fitness(create_child.kid, data, monlist,filter.multiple, round)
            round += 1
            crossover = Crossover(create_child.kid, fitness.mon,filter.multiple)
            mutate = Mutate(crossover.childMlist, crossover.childSlist,filter.multiple)
            for i in range(100):  # 原100次
                j = Fitness(mutate.kid, data, fitness.monlist,filter.multiple,round)
                if fitness.stop:
                    print("end")
                    if filter.multiple:
                        for k in fitness.endanslist:
                            if k[4] == max(map(lambda x: x[4], fitness.endanslist)):
                                remend.append(k[0])
                                remend.append(k[1])
                                remend.append(k[2])
                                remend.append(k[3])
                                remend.append(k[4])
                                print(k[2])
                                break
                    else:
                        for k in fitness.endanslist:
                            if k[2] == max(map(lambda x: x[2], fitness.endanslist)):
                                remend.append(k[0])
                                remend.append(k[1])
                                remend.append(k[2])
                                print(k)
                                print(k[0])
                                break
                    stop = 0
                    break
                crossover = Crossover(mutate.kid, fitness.mon,filter.multiple)
                mutate = Mutate(crossover.childMlist, crossover.childSlist,filter.multiple)
                round = i+1
        print('..........................................................')
        print(remend)
        ans.update({key:remend})
    print(ans)
    print("............")
    if anslist == None:
        anslist = ans
    else:
        for key, value in ans.items():
            anslist.setdefault(key, []).append(value)
    # print(anslist)
for key,value in anslist.items():
    print(value)
    if len(value[0]) == 3:
        for i in value:
            wb.append([key,i[0],i[1],i[2]])
    else:
        for i in value:
            wb.append([key,i[0],i[1],i[2],i[3],i[4]])

ws.save('D:\\result\\time_model\\' + '_TimeModel.xlsx')
