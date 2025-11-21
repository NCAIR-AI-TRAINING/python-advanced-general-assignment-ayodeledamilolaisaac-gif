import unittest
from datetime import datetime, timedelta
from main import add_visitor, EarlyEntryError, ensure_file, FILENAME
import os

class TestTimestamp(unittest.TestCase):
    def setUp(self):
        ensure_file()
        if os.path.exists(FILENAME):
            os.remove(FILENAME)
        ensure_file()

    def test_wait_time_rule(self):
        add_visitor("Bob")
        with self.assertRaises(EarlyEntryError):
            add_visitor("Alice")  # Should fail if added within 5 minutes

if __name__ == "__main__":
    unittest.main()
