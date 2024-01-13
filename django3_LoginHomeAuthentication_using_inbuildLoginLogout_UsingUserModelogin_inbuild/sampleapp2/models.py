from django.db import models

class SessionLoginInfo(models.Model):
    name=models.CharField(max_length=250)
    password=models.CharField(max_length=200)

# Create your models here.
