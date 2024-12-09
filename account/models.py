from django.db import models

class Account(models.Model):
    username = models.CharField(max_length=50)
    exp = models.IntegerField(default=0)

class Task(models.Model):
    reward = models.IntegerField(default=0)
# Create your models here.
