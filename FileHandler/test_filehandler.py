'''
SKOWRON Mateusz | Real estate market app
Github @matskowron 

September 2023
'''

from filehandler import *

import os
import tempfile
import unittest
import pandas as pd

class TestFileHandler(unittest.TestCase):
    def setUp(self):
        # Temporary file
        self.temp_file = tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False)
        self.file_path = self.temp_file.name

        # Create a sample data frame
        data = {'address': ['ul. Mazowiecka 3', 'ul. Wojska Polskiego', 'ul. Swietokrzyska', 'ul. Tamka'],
                'offer_id': [1, 2, 3, 4]}
        self.df = pd.DataFrame(data)

    def tearDown(self):
        # Remove the temporary file at the end
        os.remove(self.file_path)

    def test_read_xlsx(self):
        # Write the sample dataframe to the temporary file
        self.df.to_excel(self.file_path, index=False)
        # Create a FileHandler, reading xlsx file
        file_handler = FileHandler(self.file_path)
        xlsx = file_handler.read_xlsx()
        # Compare initial and the data frame from xlsx file
        pd.testing.assert_frame_equal(xlsx, self.df)

    def test_save_dataframe_to_xlsx_file(self):
        # Create a FileHandler, call save_dataframe_to_xlsx_file()
        file_handler = FileHandler(None)
        file_handler.save_dataframe_to_xlsx_file(self.df, self.file_path)
        # Load the saved file and compare data frames
        loaded_df = pd.read_excel(self.file_path)
        pd.testing.assert_frame_equal(loaded_df, self.df)

    def test_save_dataframe_to_xlsx_file_with_wrong_data(self):
        # Test that save_dataframe_to_xlsx_file() raises an AttributeError if the input data is not a dataframe
        file_handler = FileHandler(None)
        with self.assertRaises(AttributeError):
            file_handler.save_dataframe_to_xlsx_file('not_a_dataframe', self.file_path)

if __name__ == '__main__':
    unittest.main()