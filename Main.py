import os
from openpyxl import load_workbook

from Cut.Cut import Cut
from Format.Format import Format
from Graph.Graph import Graph
from TimeModel.TimeModel import Timemodel

DATA_DIR = "D:\\result\\src"
exe_file = []
plan_file = []

print("****File in " + DATA_DIR + "****")
for filename in os.listdir(DATA_DIR):
    print('     ' + filename)
    if filename.endswith("txt"):
        file = open(os.path.join(DATA_DIR, filename), 'r')
        exe_file.append(file)
    elif filename.endswith("xlsx"):
        file = load_workbook(os.path.join(DATA_DIR, filename))
        plan_file.append(file)
    else:
        print('!!!! ' + filename + ' is not available!!!!')

cut = Cut(exe_file, plan_file)
format = Format(cut.load_data, cut.plan_data)
# graph = Graph(format.machine_name, format.match, format.status_format, format.execute_format, format.plan_format)
timemodel = Timemodel(format.machine_name, format.match, format.execute_format, format.plan_format,
                      format.status_format)
