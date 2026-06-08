from src.driver import Driver
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