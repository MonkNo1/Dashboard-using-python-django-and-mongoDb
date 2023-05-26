from pymongo import MongoClient


def makeconnection():
    connection_string = "mongodb://localhost:27017/"
    client = MongoClient(connection_string)
    dbname = client['RawDatas']
    collections = dbname['RawData']
    return collections





# connection_string = "mongodb://localhost:27017/"
# client = MongoClient(connection_string)
# # db = client['RawDatas']
# dbname = client['RawDatas']
# checks = dbname["RawData"]

