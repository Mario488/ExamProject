from django.db import models

class Event(models.Model):
    Name = models.CharField(max_length=64)
    Description = models.TextField(max_length=255)
    Date = models.DateField()

class BookedEvent(models.Model):
    User = models.CharField(max_length=35)
    Name = models.CharField(max_length=64)