"""
fleet_manager.py

Drafted by a developer who has since rotated off the team. It started as a
simple tram registry and has been expanded several times since.

Dom has flagged this for review. He wants to know what should change before
the team builds anything else on top of it.
"""

import csv
import json
from datetime import datetime


class FleetManager:
    def __init__(self):
        self.trams = {}
        self.drivers = {}
        self.shift_assignments = []
        self.maintenance_queue = []
        self.maintenance_history = []

    def register_tram(self, tram_id, model, capacity):
        self.trams[tram_id] = {
            "tram_id": tram_id,
            "model": model,
            "capacity": capacity,
            "status": "in_service",
        }

    def get_tram(self, tram_id):
        return self.trams.get(tram_id)

    def list_trams(self):
        return list(self.trams.values())

    def list_available_trams(self):
        return [t for t in self.trams.values() if t["status"] == "in_service"]

    def register_driver(self, employee_id, name, qualified_routes, years_experience):
        self.drivers[employee_id] = {
            "employee_id": employee_id,
            "name": name,
            "qualified_routes": qualified_routes,
            "years_experience": years_experience,
        }

    def assign_driver_to_shift(self, employee_id, tram_id, route_id, start_time, end_time):
        driver = self.drivers.get(employee_id)
        if driver is None:
            raise ValueError(f"Unknown driver: {employee_id}")

        tram = self.trams.get(tram_id)
        if tram is None:
            raise ValueError(f"Unknown tram: {tram_id}")

        if route_id not in driver["qualified_routes"]:
            raise ValueError(
                f"Driver {employee_id} not qualified for route {route_id}"
            )

        if tram["status"] != "in_service":
            raise ValueError(f"Tram {tram_id} is not in service")

        self.shift_assignments.append({
            "employee_id": employee_id,
            "tram_id": tram_id,
            "route_id": route_id,
            "start_time": start_time,
            "end_time": end_time,
        })

    def get_shifts_for_driver(self, employee_id):
        return [s for s in self.shift_assignments if s["employee_id"] == employee_id]

    def get_shifts_for_tram(self, tram_id):
        return [s for s in self.shift_assignments if s["tram_id"] == tram_id]

    def schedule_maintenance(self, tram_id, scheduled_date, reason):
        if tram_id not in self.trams:
            raise ValueError(f"Unknown tram: {tram_id}")

        self.maintenance_queue.append({
            "tram_id": tram_id,
            "scheduled_date": scheduled_date,
            "reason": reason,
        })
        self.trams[tram_id]["status"] = "maintenance"

    def complete_maintenance(self, tram_id, completed_date, notes):
        self.maintenance_history.append({
            "tram_id": tram_id,
            "completed_date": completed_date,
            "notes": notes,
        })
        self.maintenance_queue = [
            m for m in self.maintenance_queue if m["tram_id"] != tram_id
        ]
        if tram_id in self.trams:
            self.trams[tram_id]["status"] = "in_service"

    def get_maintenance_history(self, tram_id):
        return [m for m in self.maintenance_history if m["tram_id"] == tram_id]

    def load_trams_from_json(self, filepath):
        with open(filepath) as f:
            data = json.load(f)
        for tram in data:
            self.trams[tram["tram_id"]] = tram

    def load_drivers_from_csv(self, filepath):
        with open(filepath) as f:
            reader = csv.DictReader(f)
            for row in reader:
                routes = row["qualified_routes"].split(";")
                self.drivers[row["employee_id"]] = {
                    "employee_id": row["employee_id"],
                    "name": row["name"],
                    "qualified_routes": routes,
                    "years_experience": int(row["years_experience"]),
                }

    def export_fleet_report_csv(self, filepath):
        with open(filepath, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["tram_id", "model", "capacity", "status"])
            for tram in self.trams.values():
                writer.writerow([
                    tram["tram_id"],
                    tram["model"],
                    tram["capacity"],
                    tram["status"],
                ])

    def export_shift_report_csv(self, filepath):
        with open(filepath, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["employee_id", "tram_id",
                            "route_id", "start_time", "end_time"])
            for shift in self.shift_assignments:
                writer.writerow([
                    shift["employee_id"],
                    shift["tram_id"],
                    shift["route_id"],
                    shift["start_time"],
                    shift["end_time"],
                ])

    def get_summary(self):
        return {
            "total_trams": len(self.trams),
            "trams_in_service": len([t for t in self.trams.values() if t["status"] == "in_service"]),
            "trams_in_maintenance": len([t for t in self.trams.values() if t["status"] == "maintenance"]),
            "total_drivers": len(self.drivers),
            "active_shifts": len(self.shift_assignments),
            "pending_maintenance": len(self.maintenance_queue),
            "report_generated_at": datetime.now().isoformat(),
        }
