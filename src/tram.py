import json

class FleetError(Exception):
    """Base exception for the Metro Tram fleet system."""

class InvalidTramError(FleetError):
    """Raised when a tram is constructed or modified with invalid data."""

class Tram:
    def __init__(self, tram_id, model, capacity, status="in_service"):
        self.tram_id = tram_id
        self.model = model
        self.capacity = capacity
        self.status = status
    
    def summary(self):
        return {
            "tram_id": self.tram_id,
            "model": self.model,
            "capacity": self.capacity,
            "status": self.status
        }

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if isinstance(value, int) and value > 0:
            self._capacity = value
        else:
            raise InvalidTramError(f"capacity must be an integer greater than 0, got {value}")

    
    @classmethod
    def from_json(cls, data):
   
        try:
            capacity = int(data["capacity"])
        
        except (KeyError, TypeError, ValueError) as e:
            raise InvalidTramError(f"Could not parse capacity from {data!r}") from e
        return cls(
            tram_id = data["tram_id"],
            model = data["model"],
            capacity = data["capacity"],
            status = data["status"]

        )
        




    def send_for_maintenance(self):
        self.status = "maintenance"

    def retire(self):
        self.status = "retired"

    def return_to_service(self):
        self.status = "in_service"

    def is_available(self):
        return self.status == "in_service"


    
