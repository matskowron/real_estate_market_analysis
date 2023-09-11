'''
SKOWRON Mateusz | Real estate market app
Github @matskowron 

September 2023
'''

import time

from tqdm import tqdm
from time import sleep
from geopy import GoogleV3, exc
from typing import List

class GeocodingAPI: 

    def __init__(self, G_MAPS_API_KEY):
        self.G_MAPS_API_KEY = G_MAPS_API_KEY

    def create_api_call_address(self, i, city='Warszawa', country='Poland'):
        '''
        Create a Google Maps API call value
        Parameters: 
            city [str]: City name

            country [str]: Country name 
        Returns:
            A string that contains the full query to the Google Maps API
        '''
        self.address =  f'{i}, {city}, {country}'
        return self.address

    def get_coordinates_from_address(self, unique_values):
        '''
        Get a location of an offer using Google Maps API. Unique values of location ['address'] are passed for cost reduction.

        Returns:
            A string that contains the full query to the Google Maps API
        '''
        location = {}
        for i in tqdm(unique_values, total=len(unique_values), desc="Status: "):
            self.create_api_call_address(i)
            self.get_offer_location()
            location.update({i: self.location_coordinates})
            sleep(.1) # to avoid exceeding the API limit  
        return location

    def get_offer_location(self) -> List[float]: 
        '''
        Get a location of an offer using Google Maps API. Unique values of location ['lokalizacja'] are passed for cost reduction. 
        Free tier, as for now, allows up to $200 of free API calls for all services. 
        For Geocoding API the cost is $5 per 1000 requests. 

        For more info see: https://mapsplatform.google.com/pricing/

        Parameters: 
            api_key [str]: requires Geocoding API key; see documentation below to generate it
            https://developers.google.com/maps/documentation/geocoding/get-api-key

        Returns: 
            A list with with floats (latitude, longitude)
        '''
        
        self.address = self.address
        geolocator = GoogleV3(api_key=self.G_MAPS_API_KEY)
        try:
            location = geolocator.geocode(self.address)
            if location is None:
                raise ValueError(f'Could not find location for {self.address}')
            self.location_coordinates =[location.latitude, location.longitude] # type: ignore
        except exc.GeopyError as e:
            raise ValueError(f'Error occurred while geocoding {self.address}: {str(e)}') from e

        return self.location_coordinates