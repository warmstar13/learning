from django.contrib.auth.models import User
from django.db import models

class Account(models.Model):
    user_info = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    exp = models.IntegerField(default=0)

    def __str__(self):
        return self.username

class Task(models.Model):
    reward = models.IntegerField(default=0)
    creator_account = models.ForeignKey(Account, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return str(self.reward)
