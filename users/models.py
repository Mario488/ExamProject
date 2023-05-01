from django.db import models

class User(models.Model):
    Roles = [
        ('A', 'Admin'),
        ('U', 'User'),
    ]
    Username = models.CharField(max_length=35, default="")
    Password = models.CharField(max_length=35, default="")
    FirstName = models.CharField(max_length=35, default="")    
    LastName = models.CharField(max_length=35, default="")  
    Role = models.CharField(max_length=1, choices=Roles)
