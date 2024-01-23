import pandas as pd
from pymongo import MongoClient


data = pd.read_csv('test.csv')

myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient['lmsbdata']
myCollection = mydb['vinylcol2']

data.reset_index(inplace=True, drop=True)

data_dict = data.to_dict("records")

myCollection.insert_many(data_dict)

myclient.close()