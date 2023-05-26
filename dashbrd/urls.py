# from django.contrib import admin
from django.urls import path
from. import views 

urlpatterns = [
    path('',views.login,name="login"),
    path('check',views.check,name="check")
]
