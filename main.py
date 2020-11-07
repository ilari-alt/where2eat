import pandas as pd
import csv
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


def create_group(groupID, userID):

    new_group = []
    new_group.append(userID)

    r = csv.reader(open('./data/groupdata.csv'))  # Here your csv file
    lines = list(r)

    print(lines)
    for line in lines:
        if line[0]==groupID:
            for i in range(len(line)):
                if line[i] == '':
                    line[i]=userID
                    break
    writer = csv.writer(open('./data/groupdata.csv', 'w', newline=''))
    writer.writerows(lines)

    r = csv.reader(open('./data/groupdata.csv'))  # Here your csv file
    lines = list(r)
    return {0:lines}


'''
    with open('./data/groupdata.csv', 'w', newline='') as outf:
            writer = csv.DictWriter(outf, fieldnames=fieldnames)
            for row in lines:
                if row["groupID"]==groupID:
                    group=row
                    for member in group:
                        print(member)
                        if len(new_group)!=5:
                            if member:
                                new_group.append(group[member])

                            else:
                                new_group.append(None)

                    writer.writerow({'groupID': groupID,
                                     'user1': new_group[0],
                                     'user2': new_group[1],
                                     'user3': new_group[2],
                                     'user4': new_group[3],
                                     'user5': new_group[4]})

                else:
                    writer.writerow(row)

                    for i in range(6 - len(new_group)):
                        new_group.append(None)'''


create_group("2","U1007")
