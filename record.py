class Record:
    def __init__(self, record_id: int, gunid: int, project: str, gun_total_shots: int, previous_record: int,
                 airline_type: str, date_time: str, airline_total_shots: int, tb_total_shots: int,
                 solenoid_total_shots: int, comments: str):
        self.record_id = record_id
        self.gunid = gunid
        self.project = project
        self.gun_total_shots = gun_total_shots
        self.previous_record = previous_record
        self.airline_type = airline_type
        self.date_time = date_time
        self.airline_total_shots = airline_total_shots
        self.tb_total_shots = tb_total_shots
        self.solenoid_total_shots = solenoid_total_shots
        self.comments = comments

    def to_tuple(self) -> tuple:
        pass