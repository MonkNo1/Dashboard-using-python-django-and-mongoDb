# from django.contrib import admin
from django.urls import path
from. import views 
db_name = "RawDatas"
host = "localhost"
port = 27017
username = "monk"
password = "monk"

urlpatterns = [
    path('',views.index,name="index")
]
