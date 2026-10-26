import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from statusline import normalize_status, summarize

class StatusTests(unittest.TestCase):
    def test_existing_statuses(self):
        for status in ["operational", "degraded", "outage"]:
            self.assertEqual(normalize_status(status), status)

    def test_case_and_spaces(self):
        self.assertEqual(normalize_status(" OPERATIONAL "), "operational")

    def test_maintenance_maps_to_degraded(self):
        self.assertEqual(normalize_status("maintenance"), "degraded")
        self.assertEqual(normalize_status(" Maintenance "), "degraded")
        self.assertEqual(normalize_status("MAINTENANCE"), "degraded")

    def test_unknown_is_not_healthy(self):
        self.assertEqual(normalize_status("banana"), "unknown")
        self.assertEqual(summarize([{"name": "API"}]), [{"name": "API", "status": "unknown"}])

if __name__ == "__main__":
    unittest.main()
