'''
Created on 5 de abr de 2018

@author: Bruno 
'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]