import json
import base64
import csv
import sys
import logging
import pymysql
from io import StringIO
import pandas as pd
from sqlalchemy import create_engine

def lambda_handler(event, context):
    endpoint = 'database-1.cujmcu3diheo.us-east-1.rds.amazonaws.com'
    username = 'admin'
    password = 'wolke.2023'
    database = 'Challenge'
    DATABASE_URL = "mysql+pymysql://{user}:{pw}@{endpoint}/{db}".format(user=username,
                                       pw=password,endpoint=endpoint,db=database)    

    try:
        engine = create_engine(DATABASE_URL)    
        file_content = str(base64.b64decode(event['content']))
        #csv_data = csv.reader(file_content)
        file_path = 'trips.csv'
        output = file_content.split('\\n')[5:-1]
        r = []
        for x in output:
            r.append(x.split(','))    
        df = pd.DataFrame(r, columns = ['region','origin_coord','destination_coord','date_trip','datasource'])
        df = df.dropna()
        rows = df.shape[0]
        df = df.drop_duplicates(subset=['origin_coord', 'destination_coord', 'date_trip'], keep="first")
        rows_duplicate = rows - df.shape[0]
        rows_inserted = df.shape[0]
    
        df.to_sql('Trip', con = engine, if_exists = 'append', chunksize = 1000, index= False)
        statusCode = 200
        body = {
            'message': 'Sucess Upload',
            'rows': rows,
            'rowsInserted': rows_duplicate,
            'rowsDuplicated': rows_duplicate            
        }

    except:
        statusCode = 400
        body = {
            'message': 'Error'
        }
    return {
        'statusCode': statusCode,
        'body': json.dumps(body)
    }