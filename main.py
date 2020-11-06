import pandas as pd
import numpy as np
#from aito.schema import AitoStringType, AitoTextType, AitoDelimiterAnalyzerSchema, AitoTableSchema, AitoColumnLinkSchema, AitoDatabaseSchema
#from aito.client import AitoClient
#import aito.api as aito_api

from pathlib import Path
# Change the data folder to where you have downloaded the original data
data_folder = (Path('.') / 'data' ).resolve()

parkinglots_data = pd.read_csv(data_folder / f'chefmozparking.csv')
cities_data = pd.read_csv(data_folder / f'geoplaces2.csv')
parkinglots_data = pd.read_csv(data_folder / f'chefmozparking.csv')

def check_parking_lot():
    valid_PID = {}
    valid_PID[0] = []
    for i in range(len(parkinglots_data)):
        if parkinglots_data["parking_lot"][i]!= "none":
            valid_PID[0].append(str(parkinglots_data["placeID"][i]))
    return valid_PID

def check_city(city):
    valid_cities = {}
    valid_cities[0] = []
    try:
        for i in range(len(parkinglots_data)):
            if parkinglots_data[city][i]!= "none":
                valid_cities[0].append(str(parkinglots_data["placeID"][i]))
    except:
        return {["error: city probably not found"]}
    return valid_cities



