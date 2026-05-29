"""
maintenance.py

A draft class for tracking maintenance jobs scheduled against a tram.

Dom thinks something might be wrong here but he hasn't had time to dig into
it. He has asked you to take a look.
"""


class MaintenanceSchedule:
    """Tracks pending maintenance jobs for a single tram."""

    pending_jobs = []

    def __init__(self, tram_id):
        self.tram_id = tram_id

    def add_job(self, description, priority="standard"):
        self.pending_jobs.append({
            "description": description,
            "priority": priority,
        })

    def get_pending_jobs(self):
        return self.pending_jobs

    def clear_jobs(self):
        self.pending_jobs = []

    def job_count(self):
        return len(self.pending_jobs)
