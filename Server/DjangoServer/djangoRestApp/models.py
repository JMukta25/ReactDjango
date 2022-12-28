from django.db import models

# Create your models here.
class User(models.Model):
    userName = models.CharField(max_length=200,primary_key=True)
    passWord = models.CharField(max_length=12)
