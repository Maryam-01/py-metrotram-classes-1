class FleetError(Exception):
    """Base exception for the Metro Tram fleet system."""

class InvalidDriverError(FleetError):
    """Raised when a driver is constructed or modified with invalid data."""

class Driver:
    def __init__(self, name, employee_id, qualified_routes, years_experience):
        self.name = name
        self.employee_id = employee_id
        self.qualified_routes = qualified_routes
        self.years_experience = years_experience

    @property
    def years_experience(self):
        return self._years_experience

    @years_experience.setter
    def years_experience(self, value):
        if isinstance(value, int) and value >= 0:
            self._years_experience = value
        else:
            raise InvalidDriverError(f"capacity must be an integer greater than 0, got {value}")

    def is_qualified_for(self, route_id):
        for route in self.qualified_routes:
            if route == route_id:
                return True
        return False

    def add_qualification(self, route_id):
        if route_id not in self.qualified_routes:
            self.qualified_routes.append(route_id)

