'''
Created on 30 de mar de 2018

@author: Bruno
'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
