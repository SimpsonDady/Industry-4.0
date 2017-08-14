import pymysql


class DataBase:
    def __init__(self, timemodel):
        self.input = timemodel
        self.open()

    def open(self):
        db = pymysql.connect('127.0.0.1', 'root', '', 'timemodel')
        sql = 'INSERT INTO summary(NUM, program, component, worknumber, nc, version, workcenter, machinename, ' \
              'startdate, starttime, enddate, endtime, spendtime) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        insert = db.cursor()
        for machine in self.input:
            for data in machine.timemodel:
                insert.execute(sql, (0, data.program, data.component, str(data.worknumber), data.nc, data.version,
                                     str(data.workcenter), data.machinename, data.startdate, data.starttime, data.enddate,
                                     data.endtime, str(data.spendtime)))
        db.commit()
