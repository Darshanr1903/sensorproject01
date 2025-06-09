from pymongo.mongo_client import MongoClient
import pandas as pd
import json
#url
uri="mongodb+srv://darshanr974151:53MRCcP5cX96tZUn@cluster0.swb8mgo.mongodb.net/?retryWrites=true&w=majority"
# create new client and connect to the server
client=MongoClient(uri)
# create database name and collection name
DATABASE_NAME="pwskills"
COLLECTION_NAME="waferfault"
df=pd.read_csv("C:\Users\HP\Downloads\Sensor_project\notebooks\wafer_23012020_041211.csv")
df=df.drop("Unnamed: 0",axis=1)
jason_record=list(json.loads(df.T.to_json()).values())
client[DATABASE_NAME][COLLECTION_NAME].insert_many(jason_record)