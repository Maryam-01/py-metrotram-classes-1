import pytest
from src.tram import Tram

def test_tram_returns_summary():
    tram = Tram("TRAM-001", "Bombardier Flexity", 200, "in_service")
    assert tram.summary() == {
            "tram_id": "TRAM-001",
            "model": "Bombardier Flexity",
            "capacity": 200,
            "status": "in_service"
    }

# A new tram exposes its tram_id, model, capacity, and status correctly
# A newly created tram defaults to "in_service" if no status is provided
# send_for_maintenance() changes the status to "maintenance"
# return_to_service() changes the status to "in_service"
# retire() changes the status to "retired"
# is_available() returns True when in service
# is_available() returns False after maintenance