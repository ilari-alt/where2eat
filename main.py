import pandas as pd
import numpy as np
import distance
#from aito.schema import AitoStringType, AitoTextType, AitoDelimiterAnalyzerSchema, AitoTableSchema, AitoColumnLinkSchema, AitoDatabaseSchema
#from aito.client import AitoClient
#import aito.api as aito_api

from pathlib import Path
# Change the data folder to where you have downloaded the original data
data_folder = (Path('.') / 'data' ).resolve()

parkinglots_data = pd.read_csv(data_folder / f'chefmozparking.csv')
cities_data = pd.read_csv(data_folder / f'geoplaces2.csv')
user_data = pd.read_csv(data_folder / f'userprofile.csv')


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
        for i in range(len(cities_data)):
            if cities_data["city"][i] != city:
                valid_cities[0].append(str(cities_data["name"][i]))
    except:
        return "error: city probably not found"
    return valid_cities


def calculate_distance(userID):
    for i in range(len(user_data)):
        if user_data["userID"][i] == userID:
            lat1 = user_data["latitude"][i]
            lon1 = user_data["longitude"][i]
            break
    restaurants = {}
    top10 = {0:[]}
    for i in range(len(cities_data)):
        d = distance.get(lat1,lon1,cities_data["latitude"][i], cities_data["longitude"][i])
        restaurants[d]=cities_data["name"][i]
    count = 0
    keylist = list(restaurants.keys())
    keylist.sort()

    for i in restaurants:
        top10[keylist[count]] = restaurants[i]
        count += 1
        if count == 10:
            break
    return top10



