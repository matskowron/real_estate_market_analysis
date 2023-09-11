'''
SKOWRON Mateusz | Real estate market app
Github @matskowron 

September 2023
'''

import os
import pandas as pd

class FileHandler():

    def __init__(self, file_path):
        self.file_path = file_path
        self.xlsx = None 

    def read_xlsx(self):
        '''
        Read a xlsx file. 

        Returns:
        '''
        file_path = os.path.join(os.getcwd(), self.file_path)
        print(f'The file {file_path} is being read.')
        self.xlsx = pd.read_excel(file_path)
        return self.xlsx

    def save_dataframe_to_xlsx_file(self, dataframe, file_path):
        """
        Save the given dataframe to a file at the specified path.

        Parameters: 
            file_path [str]: A string with a desired location
        Returns:
            An .xlsx file with the name
        """
        dataframe.to_excel(file_path, index=False)