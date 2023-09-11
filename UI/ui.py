'''
SKOWRON Mateusz | Real estate market app
Github @matskowron 

September 2023
'''
import os 

from FileChecker.filechecker import *
from FileHandler.filehandler import *
from DataProcessor.dataprocessor import *
from GeocodingAPI.geocodingapi import *
from SQLTables.sqltables import *
from GraphDrawer.graphdrawer import *

class UI:
    def run(self):

        print('\nSKOWRON Mateusz | Real estate market analyzer\nGithub @matskowron\nSeptember 2023\n')
        file_path = input('Provide the .xlsx file name:\n')
        file = FileChecker(file_path)
        if file.exists():
            while True:
                    file_content = FileHandler(file_path)
                    options = ["Show rows", "Get average price per m^2", "Get geo coordinates", "Get table from SQL database with sale per month summary", "Draw a graph with average price per m^2 for each neighborhood"]
                    print("\nAvailable options:\n" + "\n".join([f"{i}. {option}" for i, option in enumerate(options, 1)]))
                    choice = input("Type (1-5): ")
                    data_frame = file_content.read_xlsx()
                    data_processor = DataProcessor()
                    if choice == "1":
                        try:
                            top_rows_input = input("Press ENTER to display the first 10 rows, or provide the number: ")
                            top_rows = int(top_rows_input) if top_rows_input.isdigit() and int(top_rows_input) > 0 else 10
                            data_processor.head_csv(data_frame, top_rows)
                        except ValueError:
                            raise ValueError("The number of rows must be a positive integer.\n")
                        
                    elif choice == "2":
                        try:
                            skip_NaN = input("Would you like to skip NaNs while calculating:\n" + "\n".join([f"{i}. {option}" for i, option in enumerate(['Yes', 'No'], 1)]) + "\nType (1-2): ")
                            skip_NaN = True if skip_NaN == "1" else False
                            grouped_df = data_processor.mean_price_per_m2_by_offer_id(data_frame, skip_NaN)
                            file_name_mean = 'average_price_per_sqr_meter.xlsx'
                            file_content.save_dataframe_to_xlsx_file(grouped_df, file_path=file_name_mean)
                            print(f"The file named: {file_name_mean} was created.\n")
                        except KeyError:
                            print("Error: 'offer_id' and/or 'price_per_m2' columns not found in the data.")

                    elif choice == "3":
                        G_MAPS_API_KEY = input("\nPlease provide your 39-character Google Maps API key.\nIf you don't have one, you can generate it using this documentation:\nhttps://developers.google.com/maps/documentation/geocoding/get-api-key\nKey:")
                        
                        if len(G_MAPS_API_KEY) != 39:
                            print("Error: The API key should be 39 characters long.")
                        elif 'address' not in data_frame.columns:
                            print("Error: 'address' column not found in the data.")
                        else:
                            print("\nThe API key length appears to be correct.\n")
                            try:
                                unique_values = data_processor.get_unique_values(data_frame)
                                geocoding = GeocodingAPI(G_MAPS_API_KEY)
                                location = geocoding.get_coordinates_from_address(unique_values)
                                data_frame = data_processor.update_main_date_frame(data_frame, location)
                                file_content.save_dataframe_to_xlsx_file(data_frame, file_path)
                                print(f'\nThe file {file_path} has been updated with geo coordinates.\n')
                            except ValueError:
                                print("\nError: The API key is incorrect.")

                    elif choice == "4":
                        try:
                            sql = SQLTables()
                            sql.sql_table_from_dataframe()
                                
                            if "date_of_sale" not in data_frame.columns or "offer_id" not in data_frame.columns:
                                raise ValueError("Did not find 'date_of_sale' and/or 'offer_id' columns in the data.")

                            sales_data = sql.sql_data_to_populate(data_frame)
                            sql.sql_table_populate(sales_data)
                            rows = sql.sql_get_monthly_summary()
                            sql_table = sql.export_sql(rows)
                            file_content.save_dataframe_to_xlsx_file(sql_table, file_path='monthly_summary.xlsx')
                            print("The file called 'monthly_summary.xlsx' was created.\n")
                        except Exception:
                            print("Error while processing the data. Please try again")
                    elif choice == "5":
                        try:
                            if "price_per_m2" not in data_frame.columns or "neighborhood" not in data_frame.columns:
                                raise ValueError("Did not find 'price_per_m2' and/or 'neighborhood' columns in the data.")
                            graph_drawer = GraphDrawer(data_frame)
                            plot_name = graph_drawer.draw_graph()
                            print(f"The graph named {plot_name} was created.\n")

                        except Exception:
                            print("Error while processing the data. Please try again")
                    else:
                        print("Did not provide the value in range 1-5.\n\n")
        else: 
            print(f"No file with the following name was found in the folder:\n{file_path}")            
    
    def get_file_handler(self, file_path):
        """
        Check if the file at self.file_path exists and create a FileHandler instance with the path as an argument

        Returns:
            A FileHandler instance if the file exists, None otherwise.
        """

        if os.path.isfile(file_path):
            return FileHandler(file_path)
        else:
            print("Could not find the file.")
            return None