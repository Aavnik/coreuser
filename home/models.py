from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from home.manager import *

# Create your models here.
class Auser(AbstractUser):
    username= None
   
    phone_number = models.CharField(unique= True, max_length=12)
 

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELD =[]

    objects = UserManager()
