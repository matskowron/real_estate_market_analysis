# Warsaw Real estate market analyzer
This repository was created as a personal project to analyze the real estate market based on made-up data of Warsaw real estate market.

1. Prints n-th, where n = 10 by default, first records from a CSV file. 

2. Calculates mean value for a price per square meter and aggregates them by investments. It can also skip Nan values if the real estate does not have a price per square meter.

3. Calls location using Google Maps API and returns longitude and latitude in a single column.
 
4. Creates an SQL table summarizing sales in each month. This saves the data also as an XLSX file. 

5. Draws a graph showing the price per square meter for each investment in a given neighborhood. 

## Preparing the environment
This script uses additional librariers that require the install. 

Before running the code, create a virtual environment 

```bash
 python<version> -m venv <venv-name>
```

Install all required packages with the following command

```bash
 pip install -r requirements.txt
```
When having problems with installation: 
```bash
sudo pip install -r requirements.txt
```

You also need to generate an Google Maps API key, which is an argument given to the terminal. 
For more info how to generate it use: 

https://developers.google.com/maps/documentation/javascript/get-api-key

## Run the code
To run the code after installing requirements and activating the virtual environment, type: 

```python
 python3 main.py
```

## Run the tests
To run the test, go to the class folder and find the file starting with test in its name. Not all classes have tests.

```python
 python3 test_filehandler.py
```
