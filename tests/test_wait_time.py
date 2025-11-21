import unittest
import os
from main import add_visitor, ensure_file, FILENAME
from datetime import datetime, timedelta

class TestWaitTime(unittest.TestCase):
    def setUp(self):
        ensure_file()
        if os.path.exists(FILENAME):
            os.remove(FILENAME)
        ensure_file()

    def test_add_two_visitors(self):
        # Add first visitor
        add_visitor("Charlie")
        # Manually update timestamp to simulate 6 minutes later
        with open(FILENAME, "r") as f:
            name, timestamp_str = f.readline().strip().split(",")
        old_time = datetime.fromisoformat(timestamp_str) - timedelta(minutes=6)
        with open(FILENAME, "w") as f:
            f.write(f"{name},{old_time.isoformat()}\n")
        # Now adding a different visitor should pass
        add_visitor("Dana")
        with open(FILENAME, "r") as f:
            lines = f.readlines()
        self.assertEqual(len(lines), 2)

if __name__ == "__main__":
    unittest.main()
