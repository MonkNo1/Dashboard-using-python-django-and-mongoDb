# from django.contrib import admin
from django.urls import path
from. import views 

urlpatterns = [
    path('',views.login,name="login"),
    # path('charts',views.charts,name="charts"),
    path('new',views.Admin,name="New"),
    # path('getdet',views.usercheck,name="usercheck"),
    path('charts/<user>/',views.charts,name="charts"),
    path('charts/<user>/back/',views.back,name="back"),
    path('logout',views.logout,name='logout'),
    path('dash',views.dashbrd,name='dashbrd'),
    path('tabs/<user>',views.tables,name="tables"),
    path('tabs/<user>/back/',views.back),
    path('tabs/<user>/cht/<unm>',views.tableToCharts,name="tabtochr"),
    path('charts/<user>/tabs/<unm>',views.chartToTable,name="chttotable"),
    path('tabs/<user>/cht/back/',views.back),
    # path('404/',views.notFound,name="404"),
    
]
