import pytest
import json
from src.tram import Tram, FleetError, InvalidTramError


@pytest.fixture
def default_tram():
    return Tram("TRAM-001", "Bombardier Flexity", 200)


def test_tram_returns_summary(default_tram):
    assert default_tram.summary() == {
            "tram_id": "TRAM-001",
            "model": "Bombardier Flexity",
            "capacity": 200,
            "status": "in_service"
    }


def test_tram_returns_in_service(default_tram):
    assert default_tram.summary() == {
            "tram_id": "TRAM-001",
            "model": "Bombardier Flexity",
            "capacity": 200,
            "status": "in_service"
    }

def test_tram_changes_to_maintenance(default_tram):
    default_tram.send_for_maintenance()
           
    assert default_tram.summary() == {
            "tram_id": "TRAM-001",
            "model": "Bombardier Flexity",
            "capacity": 200,
            "status": "maintenance"
    }


def test_tram_retired(default_tram):
    expected = "retired"
    # act
    default_tram.retire()
    # assert
    assert default_tram.status == expected


def test_tram_in_service(default_tram):
    expected = "in_service"
    # act
    default_tram.return_to_service()
    # assert
    assert default_tram.status == expected

def test_is_available_returns_true(default_tram):
    # Act / Assert
    assert default_tram.is_available() == True

def test_is_available_returns_false(default_tram):
    # Act
    default_tram.retire()
    # Assert
    assert default_tram.is_available() == False

def test_tram_capacity_raises_error_if_negative(): 
    with pytest.raises(InvalidTramError):
        tram = Tram("TRAM-001", "Bombardier Flexity", -200, "in_service")

def test_tram_capacity_raises_error_if_zero(): 
    with pytest.raises(InvalidTramError):
        tram = Tram("TRAM-001", "Bombardier Flexity", 0, "in_service")

def test_from_json_returns_tram_id():
    tram = Tram.from_json( {
    "tram_id": "TRAM-001",
    "model": "Bombardier Flexity",
    "capacity": 200,
    "status": "in_service"
  })
    
    assert tram.tram_id == "TRAM-001"

def test_from_json_returns_capacity():
    tram = Tram.from_json( {
    "tram_id": "TRAM-001",
    "model": "Bombardier Flexity",
    "capacity": 200,
    "status": "in_service"
  })
    
    assert tram.capacity == 200



