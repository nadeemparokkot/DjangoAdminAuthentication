from django.contrib import admin
from . models import MovieInfo #this for create a our movieinfo model(database table) in admin interface  

# Register your models here.
admin.site.register(MovieInfo) 