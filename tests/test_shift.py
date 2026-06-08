import pytest
from src.shift import Shift

@pytest.fixture
def default_shift():
    return Shift("SHF-2024-001",
    "EMP-1001",
    "TRAM-001",
    "route_1",
    "2024-11-18T05:30:00",
    "2024-11-18T13:30:00"
    )





def test_returns_length_of_shift_as_float(default_shift):
    expected = 8.0
    
    # assert
    assert default_shift.duration_hours() == expected

def test_returns_attributes(default_shift):
    assert default_shift.shift_id == "SHF-2024-001"
    