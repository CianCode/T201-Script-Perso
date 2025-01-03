import unittest
import os
from src.data_handler import CustomDataGen

class TestCustomDataGen(unittest.TestCase):
    def setUp(self):
        self.data_gen = CustomDataGen()
        self.data_gen.remove_files()  # Clean up any pre-existing files

    def tearDown(self):
        self.data_gen.remove_files()  # Clean up after the test

    def test_create_files(self):
        self.data_gen.create_files(3, 5)
        files = os.listdir(self.data_gen.data_path)
        self.assertEqual(len(files), 3)  # Expect 3 files to be created

    def test_remove_files(self):
        self.data_gen.create_files(2, 5)
        self.data_gen.remove_files()
        files = os.listdir(self.data_gen.data_path)
        self.assertEqual(len(files), 0)  # Expect all files to be deleted

if __name__ == "__main__":
    unittest.main()
