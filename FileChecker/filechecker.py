'''
SKOWRON Mateusz | Real estate market app
Github @matskowron 

September 2023
'''

class FileChecker:
    def __init__(self, filename):
        self.filename = filename
        
    def exists(self):
        import os
        return os.path.isfile(self.filename)