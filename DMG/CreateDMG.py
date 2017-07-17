from DMG.Method.CutData import CutData
from DMG.Method.CutWorkList import Cutworklist
from DMG.Method.Format import Format


class CreateDMG:
    def __init__(self, execute_file, plan_file):
        self.execute_cut = None
        self.plan_cut = None
        self.machine_name = ''

        self.status_spend = None
        self.execute_spend = None
        self.plan_spend = None

        self.y_high = None
        self.y_tick = None

        self.cut(execute_file, plan_file)
        self.format()
        
    def cut(self, execute_file, plan_file):
        print('Data Cutting...')
        self.execute_cut = CutData(execute_file)
        self.plan_cut = Cutworklist(plan_file)
        if self.execute_cut.machine_name == '9703':
            self.machine_name = 'DMG01'
        elif self.execute_cut.machine_name == '9702':
            self.machine_name = 'DMG02'
        else:
            self.machine_name = ''
        print('done')

    def format(self):
        print('Data Formatting...')
        format_data = Format(self.execute_cut.date, self.execute_cut.time)
        self.status_spend = format_data.build(self.execute_cut.work)
        self.execute_spend = format_data.build(self.execute_cut.code,
                                               self.execute_cut.component, self.execute_cut.version)
        self.plan_spend = format_data.build(self.plan_cut.code, None, None,
                                            self.plan_cut.start_date, self.plan_cut.start_time,
                                            self.plan_cut.end_date, self.plan_cut.end_time)
        for i in self.execute_spend:
            i.printAll()
        print('done')
