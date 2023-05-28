# from django.contrib import admin
from django.urls import path
from. import views 

urlpatterns = [
    path('',views.login,name="login"),
    path('check',views.check,name="check"),
    # path('charts',views.charts,name="charts"),
    path('new',views.Admin,name="New"),
    path('getdet',views.usercheck,name="usercheck"),
    path('charts/<user>/',views.charts,name="charts"),
    path('charts/<user>/back/',views.back,name="back")
]
