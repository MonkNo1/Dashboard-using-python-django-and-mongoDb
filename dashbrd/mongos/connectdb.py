from pymongo import MongoClient


connection_string = "mongodb://localhost:27017/"
client = MongoClient(connection_string)


def userconnection():
    dbname = client['RawDatas']
    collections = dbname['Admins']
    return collections


def makeconnection():
    dbname = client['RawDatas']
    collections = dbname['RawData']
    return collections




# connection_string = "mongodb://localhost:27017/"
# client = MongoClient(connection_string)
# # db = client['RawDatas']
# dbname = client['RawDatas']
# checks = dbname["RawData"]

