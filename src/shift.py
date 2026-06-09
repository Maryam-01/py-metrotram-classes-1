# duration_hours(): returns the length of the shift as a float, calculated from start_time and end_time. Use datetime.fromisoformat() to parse the strings.
from datetime import datetime

class FleetError(Exception):
    """Base exception for the Metro Tram fleet system."""

class InvalidShiftError(FleetError):
    """Raised when a shift is constructed or modified with invalid data."""

class Shift:
    def __init__(self, shift_id, driver_id, tram_id, route_id, start_time, end_time):
        self.shift_id = shift_id
        self.driver_id = driver_id
        self.tram_id = tram_id
        self.route_id = route_id
        self.start_time = start_time
        self.end_time = end_time

    @property
    def end_time(self):
        return self._end_time
    
    @end_time.setter
    def end_time(self, value):
        if value > self.start_time:
            self._end_time = value
        else:
            raise InvalidShiftError(f"start_time must be before end_time")

    def duration_hours(self):
        start = datetime.fromisoformat(self.start_time)
        end = datetime.fromisoformat(self.end_time)

        duration = end - start
        seconds = duration.total_seconds()
        minutes = seconds/60
        hours = minutes/60
        return hours
        




