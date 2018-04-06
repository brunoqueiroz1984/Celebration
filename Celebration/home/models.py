from django.db import models 
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
    event_type = models.CharField(max_length = 11, choices = EVENTS_TYPES)
    tags = models.CharField(max_length = 200)
    permissions = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.name
    
class Promoter(models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 50)
    password = models.CharField(max_length = 20)
    permissions_promoter = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.name

class Admin(models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 50)
    password = models.CharField(max_length = 20)
    permissions_adm = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.name
    
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
    event_type = models.CharField(max_length = 11, choices = EVENTS_TYPES)
    tags = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.name
    
class Place(models.Model):
    name = models.CharField(max_length = 100)
    address = models.TextField()
    tags = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.name