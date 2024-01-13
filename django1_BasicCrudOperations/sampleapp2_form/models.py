from django.db import models

# Create your models here.
class MovieInfo(models.Model):
    head=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    descrption=models.TextField()
    image = models.FileField(default='/home/hp/Downloads/brain_05.png')
   

    