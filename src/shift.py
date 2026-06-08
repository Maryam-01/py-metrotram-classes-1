# duration_hours(): returns the length of the shift as a float, calculated from start_time and end_time. Use datetime.fromisoformat() to parse the strings.

from datetime import datetime

class Shift:
    def __init__(self, shift_id, driver_id, tram_id, route_id, start_time, end_time):
        self.shift_id = shift_id
        self.driver_id = driver_id
        self.tram_id = tram_id
        self.route_id = route_id
        self.start_time = start_time
        self.end_time = end_time

    def duration_hours(self):
        start = datetime.fromisoformat(self.start_time)
        end = datetime.fromisoformat(self.end_time)

        duration = end - start
        seconds = duration.total_seconds()
        minutes = seconds/60
        hours = minutes/60
        return hours
        




