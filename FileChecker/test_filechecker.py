'''
SKOWRON Mateusz | Real estate market app
Github @matskowron 

September 2023
'''

from filechecker import *

import unittest
import os
from tempfile import NamedTemporaryFile

class TestFileChecker(unittest.TestCase):
    
    def test_file_exists(self):
        with NamedTemporaryFile(delete=False) as temp_file:
            file_checker = FileChecker(temp_file.name)
            self.assertTrue(file_checker.exists())
            os.unlink(temp_file.name)

    def test_file_does_not_exist(self):
        with NamedTemporaryFile(delete=False) as temp_file:
            temp_file_path = temp_file.name
        file_checker = FileChecker(temp_file_path + '_nonexistent')
        self.assertFalse(file_checker.exists())
    
if __name__ == '__main__':
    unittest.main()