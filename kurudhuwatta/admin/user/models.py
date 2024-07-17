


from django.db import models
from django.contrib.auth.models import User

class UserRegister(models.Model):
    
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    adress = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

  
