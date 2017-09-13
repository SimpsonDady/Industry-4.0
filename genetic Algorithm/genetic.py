import time

from openpyxl import Workbook

from method.CreateChlid import CreateChild
from method.Crossover import Crossover
from method.Filter import Filter
from method.Fitness import Fitness
from method.Mutate import Mutate
from method.ReadFile import ReadFile

readfile = ReadFile()
ans = {}
for key, value in readfile.information.items():
    filter = Filter(value)
    data = filter.outdata
    print(data)
    stop = True
    remend = []
    monlist = []
    while stop:
        create_child = CreateChild(filter.multiple)
        fitness = Fitness(create_child.kid, data, monlist,filter.multiple)
        crossover = Crossover(create_child.kid, fitness.mon,filter.multiple)
        mutate = Mutate(crossover.childMlist, crossover.childSlist,filter.multiple)
        for i in range(100):
            fitness = Fitness(mutate.kid, data, fitness.monlist,filter.multiple)
            if fitness.stop:
                print("end")
                print(fitness.monlist)
                print(fitness.monlist[-1][0])
                remend.append(fitness.monlist[-1][0])
                if filter.multiple:
                    remend.append(fitness.monlist[-1][2])
                    print(fitness.monlist[-1][2])
                stop = 0
                break
            crossover = Crossover(mutate.kid, fitness.mon,filter.multiple)
            mutate = Mutate(crossover.childMlist, crossover.childSlist,filter.multiple)
    print('..........................................................')
    print(remend)
    ans.update({key:remend})
print(ans)
ws = Workbook()
wb = ws.active
wb.append(['工具代碼', '一件時間','兩件時間'])
for key,value in ans.items():
    print(value)
    if len(value) == 1:
        wb.append([key,value[0]])
    else:
        wb.append([key,value[0],value[1]])
ws.save('D:\\result\\time_model\\' + '_TimeModel.xlsx')
