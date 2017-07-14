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

        # self.status_daily = None
        # self.execute_daily = None
        # self.plan_daily = None

        self.y_high = None
        self.y_tick = None

        self.cut(execute_file, plan_file)
        self.format()
        # self.daily()
        
    def cut(self, execute_file, plan_file):
        print('Data Cutting...')
        self.execute_cut = CutData(execute_file)
        self.plan_cut = Cutworklist(plan_file)
        self.machine_name = self.execute_cut.machine_name
        print('done')

    def format(self):
        print('Data Formatting...')
        format_data = Format(self.execute_cut.date, self.execute_cut.time)
        self.status_spend = format_data.build(self.execute_cut.work)
        self.execute_spend = format_data.build(self.execute_cut.code)
        self.plan_spend = format_data.build(self.plan_cut.code,
                                            self.plan_cut.start_date, self.plan_cut.start_time,
                                            self.plan_cut.end_date, self.plan_cut.end_time)
        print('done')

    # def daily(self):
    #     print('Translating to daily form...')
    #     final = Daily(self.status_spend, self.execute_spend, self.plan_spend)
    #     self.status_daily = final.status
    #     self.execute_daily = final.execute
    #     self.plan_daily = final.plan
    #     self.y_high = final.y_high
    #     self.y_tick = final.y_tick
    #     print('done')
