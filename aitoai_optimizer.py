import os
import pandas as pd
from functools import reduce
import numpy as np
from aito.schema import AitoStringType, AitoTextType, AitoDelimiterAnalyzerSchema, AitoTableSchema, AitoColumnLinkSchema, AitoDatabaseSchema
from aito.client import AitoClient
import aito.api as aito_api
from pathlib import Path

totally_not_api_key = "X5FsYeAPc82wjsLOqQtyONmJC6XOqmo4iDTOjxKj"
data_folder = (Path('.') / 'data' ).resolve()
places_accept_df = pd.read_csv(data_folder / f'chefmozaccepts.csv')
print(places_accept_df)

places_accept_df.rename(columns={'Rpayment': 'payment'}, inplace=True)
places_accept_df = places_accept_df.groupby('placeID').agg({'payment': lambda x: ';'.join(x)}).reset_index()
users_profile_df = pd.read_csv(data_folder / 'userprofile.csv')
places_cuisine_df = pd.read_csv(data_folder / f'chefmozcuisine.csv')
users_cuisine_df = pd.read_csv(data_folder / 'usercuisine.csv')
places_parking_df = pd.read_csv(data_folder / f'chefmozparking.csv')
places_hours_df = pd.read_csv(data_folder / f'chefmozhours4.csv')
places_geo_df = pd.read_csv(data_folder / f'geoplaces2.csv', encoding='latin-1')
users_payment_df = pd.read_csv(data_folder / 'userpayment.csv')

places_df = reduce(lambda left,right: pd.merge(left, right, on='placeID', how='outer'),
                   [places_accept_df, places_cuisine_df, places_parking_df, places_hours_df, places_geo_df])
places_df.placeID = places_df.placeID.astype(str)
places_df.replace({np.nan: None}, inplace=True)
users_df = reduce(lambda left,right: pd.merge(left, right, on='userID', how='outer'),
                  [users_profile_df, users_cuisine_df, users_payment_df])
users_df.replace({np.nan: None}, inplace=True)
ratings_df = pd.read_csv(data_folder / 'rating_final.csv')
ratings_df.placeID = ratings_df.placeID.astype(str)

places_schema = AitoTableSchema.infer_from_pandas_data_frame(places_df)
users_schema = AitoTableSchema.infer_from_pandas_data_frame(users_df)
ratings_schema = AitoTableSchema.infer_from_pandas_data_frame(ratings_df)

for field in ('payment', 'cuisine'):
    users_schema[field].data_type = AitoTextType()
    users_schema[field].analyzer = AitoDelimiterAnalyzerSchema(delimiter=';')

db_schema = AitoDatabaseSchema(tables={'users': users_schema, 'places': places_schema, 'ratings': ratings_schema})

client = AitoClient(instance_url=AITO_INSTANCE_URL, api_key=AITO_API_KEY)
