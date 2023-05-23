from django.shortcuts import render
from django.http import HttpResponse
from pymongo import MongoClient

connection_string = "mongodb://localhost:27017/"
client = MongoClient(connection_string)
# db = client['RawDatas']
dbname = client['RawDatas']
checks = dbname["RawData"]


# Create your views here.
def index(request):
    # return render("Hii")
    counts = checks.find({})
    # print(counts) 
    for r in counts:
        print(r["_id"])  
    cnt = "hgiii"
    return HttpResponse(cnt)
