'''
SKOWRON Mateusz | Real estate market app
Github @matskowron 

September 2023
'''

from UI import *
import pandas as pd

class DataProcessor:

    def head_csv(self, dataframe, top_rows = 10):
        '''
        Print n-th first records from a CSV file.

        Parameters: 
            top_rows [int]: Number of rows to return; rows counted from the top

        Returns: 
            Prints the given number of rows
        '''
        print(dataframe.head(top_rows)) 

    def mean_price_per_m2_by_offer_id(self, dataframe, skip_NaNs = False):
        '''
        Returns the mean value of 'price_per_m2' grouped by 'offer_id', does not skip NaNs

        Returns:
            A Pandas series with the mean value of 'price_per_m2' grouped by 'offer_id'.
        '''
        if skip_NaNs == False:
            grouped_df = dataframe.groupby(['offer_id']).agg({'price_per_m2': 'mean'}).reset_index()
        else:
            grouped_df = dataframe.dropna(subset=['price_per_m2']).groupby(['offer_id']).agg({'price_per_m2': 'mean'}).reset_index()
        return grouped_df

    def get_unique_values(self, dataframe, column = 'address'):
        '''
        Creates a data frame with only unique values for a given column. 

        Parameters:
        column [str]: String with a column name that is checked for duplicates; Default = 'address' 
        '''
        unique_values = dataframe[column].drop_duplicates().reset_index(drop=True).to_list()  
        return unique_values
    
    def update_main_date_frame(self, data_frame, location, column = 'address'):
        '''
        Map the dataframe with the received values of location 

        Parameters:
        data_frame [data_frame]: Dataframe from xlsx file.

        location [dict]: Dictionary with key as address and value as location
        '''
        data_frame['geo_coordinates'] = data_frame[column].map(location)
        return data_frame