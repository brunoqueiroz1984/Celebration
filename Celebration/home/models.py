from django.db import models
from djangotoolbox.fields import ListField
# Create your models here.

class User(models.Model):
    RESTAURANTS = "Restaurants"
    BARS = "Bars"
    BALLADS = "Ballads"
    MOVIES = "Movies"
    THEATERS = "Theaters"
    EVENTS_TYPES = (
        (RESTAURANTS, "Restaurants"),
        (BARS, "Bars"),
        (MOVIES, "Movies"),
        (THEATERS, "Theaters"),
    )
    
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 50)
    password = models.CharField(max_length = 20)
    event_type = models.CharField(max_lenth = 5, choices = EVENTS_TYPES)
    tags = ListField()
    permissions = ListField()
    
class Promoter(models.Model, User):
    permissions_promoter = ListField()

class Admin(models.Model, User):
    permissions_adm = ListField()
    
class Event(models.Model):
    
    RESTAURANTS = "Restaurants"
    BARS = "Bars"
    BALLADS = "Ballads"
    MOVIES = "Movies"
    THEATERS = "Theaters"
    EVENTS_TYPES = (
        (RESTAURANTS, "Restaurants"),
        (BARS, "Bars"),
        (MOVIES, "Movies"),
        (THEATERS, "Theaters"),
    )
    
    name = models.CharField(max_length = 100)
    event_type = models.CharField(max_lenth = 5, choices = EVENTS_TYPES)
    tags = ListField()
    
class Place(models.Model):
    name = models.CharField(max_length = 100)
    address = models.TextField()
    tags = ListField()
    


    