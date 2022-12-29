from django.db import models

# Create your models here.
class User(models.Model):
    userName = models.CharField(max_length=200,primary_key=True)
    passWord = models.CharField(max_length=12)

class ticket(models.Model): 
    id = models.IntegerField(primary_key=True)
    ticket_img = models.URLField(max_length=500)
    ticket_name = models.CharField(max_length=400) 
    ticket_func = models.CharField(max_length=10000) 
    