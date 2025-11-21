import unittest
import os
from main import ensure_file, FILENAME

class TestFileCreation(unittest.TestCase):
    def setUp(self):
        if os.path.exists(FILENAME):
            os.remove(FILENAME)

    def test_file_creation(self):
        ensure_file()
        self.assertTrue(os.path.exists(FILENAME))

if __name__ == "__main__":
    unittest.main()
