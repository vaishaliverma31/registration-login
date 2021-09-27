from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    username=models.CharField(max_length=50,unique=True)
    password=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    first_name=models.CharField(max_length=111)
    last_name=models.CharField(max_length=111)