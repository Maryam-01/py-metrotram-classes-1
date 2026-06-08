class Tram:
    def __init__(self, tram_id, model, capacity, status):
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


# send_for_maintenance(): changes the tram's status to "maintenance"
# return_to_service(): changes the tram's status to "in_service"
# retire(): changes the tram's status to "retired"
# is_available(): returns True if the tram is in service, otherwise False