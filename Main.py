from Method.CutData import CutData
from Method.CutWorkList import Cutworklist
from Method.Format import Format
from Method.Final import Final

print('Data Cutting...')
cut_data = CutData('DMG01_0703-0707.txt')
work_list = Cutworklist('DMG01_0703-0707.xlsx')
print('done')
print('Data Formatting...')
format_data = Format(cut_data.date, cut_data.time)
runSpend = format_data.build(cut_data.work)
programSpend = format_data.build(cut_data.code)
workSpend = format_data.build(work_list.code, work_list.start_date, work_list.start_time, work_list.end_date, work_list.end_time)
print('done')
print('Graphing...')
final = Final(runSpend, programSpend, workSpend)
print('done')
