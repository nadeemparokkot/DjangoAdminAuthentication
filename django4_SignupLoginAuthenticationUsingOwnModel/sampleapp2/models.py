from django.db import models
from django.contrib.auth.hashers import make_password  # Import for password hashing

class LoginInfo(models.Model):
    name = models.CharField(max_length=250)
    password = models.CharField(max_length=255)  # Increased max_length for flexibility
    
    