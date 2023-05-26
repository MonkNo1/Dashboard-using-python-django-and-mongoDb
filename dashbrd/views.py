from django.shortcuts import render
from django.http import HttpResponse
from . import connectdb
import numpy as np
import operator as op


coll  = connectdb.makeconnection()

def database_fetch():
    intensity = []
    intensity_count = []
    country = []
    country_count = []
    temptab = []
    tabl = []
    counts = coll.find({})
    for r in counts:
        temptab.append(r["sector"])
        temptab.append(r["intensity"])
        temptab.append(r["topic"])
        temptab.append(r["source"])
        temptab.append(r["likelihood"])
        temptab.append(r["relevance"])
        tabl.append(temptab)
        temptab = []
        if r["intensity"] == '' or r["country"] == "": 
            continue
        intensity.append(int(r["intensity"]))
        country.append(r['country'])
        unique_intensity = list(set(intensity))
        unique_country = list(set(country))
    # print(len(unique_country))
    for i in unique_intensity:
        # print(i," = ", op.countOf(intensity, i))
        intensity_count.append(op.countOf(intensity, i))
    for i in unique_country:
        # print(i," = ", op.countOf(country, i))
        country_count.append(op.countOf(country, i))
    context = {
        "label_va" : unique_intensity,
        "data" : intensity_count,
        "Totintensity" : len(unique_intensity),
        "totcountry" : len(unique_country),
        "country" : unique_country,
        "country_count": country_count,
        "tab" : tabl
    }
    return context
    
#logical error 
def charttest():
    counts = coll.find({})
    years = []
    yearc = []
    for i in counts:
        val = i["published"].split(" ")
        try:
            years.append(int(val[2]))            
    # print(uni_year)
        except:
            pass
    uni_year = list(set(years))
    for i in uni_year:
        yearc.append(op.countOf(years,i))    
    print(yearc)
    context = {
        'yearlab' : uni_year,
        'ycunt'   : yearc
    }
    return context
#end of Logical error 
def charts(request):
    context = charttest()
    return render(request,"charts.html",context)
    
# Create your views here.
def check(request):
    return render(request,"base-copy.html")

def login(request):
    # return render(request,"login.html")
    if request.method == "POST":
        if request.method == 'POST':
            # print("method check")
            uname = request.POST['name']
            passw = request.POST['passw']   
            if uname == "admin" and passw == "admin":
                context = database_fetch()
                context['user'] = uname
                return render(request,"index.html",context)
            else:
                return render(request,"login.html")
    else :
        return render(request,"login.html")
        