from django.db import models

class User(models.Model):
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    email = models.CharField(max_length = 40)

class Cat(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length = 20)
# Create your models here.
