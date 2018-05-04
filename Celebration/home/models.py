from django.db import models 
from pymongo import mongo_client
# Create your models here.

DB_NAME = 'celebration' 
DB_HOST = 'ds161529.mlab.com'
DB_PORT = 61529
DB_USER = 'admin' 
DB_PASS = '1234'

connection = mongo_client.MongoClient(DB_HOST, DB_PORT)
db = connection[DB_NAME]
db.authenticate(DB_USER, DB_PASS)

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
    profilePhoto = models.CharField(max_length = 10)
    
    def __str__(self):
        return self.name
    
    def saveUser(self):
        user = {}
        user['name'] = self.name
        user['email'] = self.email
        user['password'] = self.password
        user['event_type'] = self.event_type
        user['tags'] = self.tags
        user['permissions'] = self.permissions
        user['profilePhoto'] = self.profilePhoto
        if(db['users'].find_all({'name':user['name']}) == [{}]):
            db['users'].insert(user)
        
    
    def getUserByName(self, userName):
        return db['users'].find_one({'name':userName})
    
class Promoter(models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 50)
    password = models.CharField(max_length = 20)
    permissions_promoter = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.name
    
    def savePromoter(self):
        promoter = {}
        promoter['name'] = self.name
        promoter['email'] = self.email
        promoter['password'] = self.password
        promoter['permissions'] = self.permissions_promoter
        if(db['promoters'].find_all({'name':promoter['name']}) == [{}]):
            db['promoters'].insert(promoter)
    
    def getPromoterByName(self, promoterName):
        return db['promoters'].find_one({'name':promoterName})
    
    def getAllPromoters(self):
        return db['promoters'].find()

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
    date = models.DateField()
    telephone = models.CharField(max_length = 19)
    price = models.DecimalField(max_digits=5, decimal_places = 2)
    time = models.TimeField() 
    
    def __str__(self):
        return self.name
    
    def getAllEvents(self):
        return db['events'].find()
    
    def getAllEventsByType(self, eventType):
        return db['events'].find({'eventType':eventType})
    
    def saveEvent(self, place):
        event = {}
        event['name'] = self.name
        event['address'] = place.address
        event['event_type'] = self.event_type
        event['tags'] = self.tags
        event['date'] = self.date
        event['telephone'] = self.telephone
        event['price'] = self.price
        event['time'] = self.time
        if(db['events'].find_all({'name':event['name']}) == [{}]):
            db['events'].insert(event)
        
    def getEventByName(self, eventName):
        return db['events'].find_one({'name':eventName})
    
    def getAllEventsByTags(self, eventTag):
        return db['events'].find({'tag':{eventTag}})
    
    def getAllEventsByPrice(self, price):
        return db['events'].find({'price':{"$lt": price}})
    
    def getAllEventsByPlace(self, place):
        return db['events'].find({'address':place})
        
    
class Place(models.Model):
    name = models.CharField(max_length = 100)
    address = models.TextField()
    tags = models.CharField(max_length = 50)
    number = models.DecimalField(max_digits= 5,decimal_places = 2)
    
    def __str__(self):
        return self.name