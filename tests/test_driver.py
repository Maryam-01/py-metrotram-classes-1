from src.driver import Driver, FleetError, InvalidDriverError
import pytest

@pytest.fixture
def default_driver():
    return Driver("EMP-1002","Jennifer Asare",["route_1","route_2","route_3"],18)

def test_is_qualified_returns_true(default_driver):
    assert default_driver.is_qualified_for("route_1") == True

def test_is_qualified_returns_false(default_driver):
    assert default_driver.is_qualified_for("route_4") == False

def test_add_qualification_adds_new_route(default_driver):
    default_driver.add_qualification("route_4")
    assert default_driver.qualified_routes == ["route_1","route_2","route_3", "route_4"]

def test_add_qualification_doesnt_add_duplicates(default_driver):
    default_driver.add_qualification("route_3")
    assert default_driver.qualified_routes == ["route_1","route_2","route_3"]

def test_driver_years_experience_raises_error_if_negative(): 
    with pytest.raises(InvalidDriverError):
        driver = Driver("EMP-1002","Jennifer Asare",["route_1","route_2","route_3"], -10)

        
def test_driver_converts_csv_returns_years_experience():
    driver = Driver.from_csv_row("EMP-1001,Marcus Whitfield,route_1;route_2,12")
        
    assert driver.years_experience == 12

def test_driver_returns_driver_name():
    driver = Driver.from_csv_row("EMP-1001,Marcus Whitfield,route_1;route_2,12")
        
    assert driver.name == "Marcus Whitfield"

def test_driver_id_returns_driver_id():
    driver = Driver.from_csv_row("EMP-1001,Marcus Whitfield,route_1;route_2,12")
        
    assert driver.employee_id == "EMP-1001"

def test_driver_qualified_routes_returns_qualified_routes():
    driver = Driver.from_csv_row("EMP-1001,Marcus Whitfield,route_1;route_2,12")
        
    assert driver.qualified_routes == ["route_1", "route_2"]

    
