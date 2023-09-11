'''
SKOWRON Mateusz | Real estate market app
Github @matskowron 

September 2023
'''

import sqlite3
import pandas as pd

class SQLTables:
    
    def sql_table_from_dataframe(self, sql_database = 'monthly_sales'):
        '''
        Create an SQL base of a given name
        
        Parameters:
            sql_database [str]: String with a column name. Default = 'address' 
        
        Returns:
            An instance sql_database, later used as parametr
        '''
        conn = sqlite3.connect(sql_database) 
        c = conn.cursor()
        sql_create_tabel =f'''
        CREATE TABLE IF NOT EXISTS f{sql_database}
                (property_id INTEGER PRIMARY KEY, date_of_sale DATE)
        '''
        c.execute(sql_create_tabel)
        self.sql_database = sql_database
        return self.sql_database

    def sql_data_to_populate(self, dataframe):
        '''
        Create an SQL base of a given name

        Returns: 
            A dataframe w 2 columns used for creating a summary
        '''
        sales_data = dataframe.copy()
        sales_data = sales_data.loc[:, ['property_id', 'date_of_sale']]
        return sales_data

    def sql_table_populate(self, sales_data):
        '''
        Populate the SQL table with records
        '''
        conn = sqlite3.connect(self.sql_database) 
        conn.cursor()
        sales_data.to_sql(self.sql_database, conn, if_exists='replace', index = False)
        conn.commit()

    def sql_get_monthly_summary(self): 
        '''
        Create an SQL databasebase
        
        Returns: 
            SQL result as list
        '''
        conn = sqlite3.connect(self.sql_database) 
        c= conn.cursor()
        sql = f'''
        SELECT 
            STRFTIME('%Y', date_of_sale) AS year,
            STRFTIME('%m', date_of_sale) AS month,
            COUNT(property_id) AS num_of_properties_sold
            FROM '{self.sql_database}' 
            GROUP BY year, month
        '''
        c.execute(sql)
        rows = c.fetchall()
        return rows 
    
    def export_sql(self, rows):
        '''
        Export list as a dataframe
        
        Returns: 
            A pandas dataframe 
        '''
        sql_table = pd.DataFrame(rows, columns=['Year', 'Month', 'Sold properties'])
        return sql_table 