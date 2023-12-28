from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length= 50,null=False, unique = True)
    department = models.CharField(max_length= 50)
    phone = models.CharField(max_length = 15)
    password = models.CharField(max_length = 59)

    def __str__(self):
        return self.first_name