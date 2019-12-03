from . import views
from django.urls import path
from home.dash_apps.finished_apps import simpleexample

urlpatterns = [
    path('', views.home, name='home'),
    path('graph/', views.graph, name='graph'),
    path('table/', views.table, name='table'),
    path('chart/', views.chart, name='chart'),
    path('pie/', views.pie, name='pie'),
    path('tree/', views.tree, name='tree'),
    path('result/', views.result, name='result'),
]
