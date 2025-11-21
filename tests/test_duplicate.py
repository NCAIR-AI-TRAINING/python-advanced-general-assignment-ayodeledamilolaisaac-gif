import unittest
import os
from main import add_visitor, DuplicateVisitorError, ensure_file, FILENAME

class TestDuplicateVisitor(unittest.TestCase):
    def setUp(self):
        ensure_file()
        # Start fresh for each test
        if os.path.exists(FILENAME):
            os.remove(FILENAME)
        ensure_file()

    def test_duplicate(self):
        add_visitor("Alice")
        with self.assertRaises(DuplicateVisitorError):
            add_visitor("Alice")  # Adding same visitor consecutively

if __name__ == "__main__":
    unittest.main()
