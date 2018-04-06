from django.contrib import admin
from home.models import Event,Place,Promoter,User,Admin
# Register your models here.

admin.site.register(Event)
admin.site.register(Place)
admin.site.register(Promoter)
admin.site.register(User)
admin.site.register(Admin)
