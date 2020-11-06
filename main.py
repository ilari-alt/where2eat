import pandas as pd
import numpy as np
#from aito.schema import AitoStringType, AitoTextType, AitoDelimiterAnalyzerSchema, AitoTableSchema, AitoColumnLinkSchema, AitoDatabaseSchema
#from aito.client import AitoClient
#import aito.api as aito_api

from pathlib import Path
# Change the data folder to where you have downloaded the original data
data_folder = (Path('.') / 'data' ).resolve()

places_accept_df = pd.read_csv(data_folder / f'chefmozparking.csv')



def check_parking_lot():
    valid_PID = {}
    valid_PID[0] = []
    for i in range(len(places_accept_df)):
        if places_accept_df["parking_lot"][i]!="none":
            valid_PID[0].append(str(places_accept_df["placeID"][i]))
    return valid_PID



