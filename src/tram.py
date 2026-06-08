

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

    def send_for_maintenance(self):
        self.status = "maintenance"

    def retire(self):
        self.status = "retired"

    def return_to_service(self):
        self.status = "in_service"

    def is_available(self):
        return self.status == "in_service"


    
