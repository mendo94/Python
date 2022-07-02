from datetime import datetime


class PoolTables:
    def __init__(self, table_number):
        self.table_number = table_number
        self.start_time = None
        self.end_time = None
        self.is_occupied = False
        self.total_time_played = None

    def check_out(self):
        if self.is_occupied == False:
            self.is_occupied = True
            self.start_time = datetime.now()
            self.converted_start_time = self.start_time.strftime("%H:%M")

    def cash_in(self):
        if self.is_occupied == True:
            self.is_occupied = False
            self.end_time = datetime.now()
            self.converted_end_time = self.end_time.strftime("%H:%M")
            self.total_time_played = (self.start_time - self.end_time)
