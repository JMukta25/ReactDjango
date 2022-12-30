from django.db import models

# Create your models here.
class User(models.Model):
    userName = models.CharField(max_length=200,primary_key=True)
    passWord = models.CharField(max_length=12)

class ticket(models.Model): 
    id = models.IntegerField(primary_key=True)
    ticket_image = models.URLField(max_length=500)
    ticket_name = models.CharField(max_length=400) 
    ticket_func = models.CharField(max_length=10000) 
    

class userHistory(models.Model): 
    userName = models.ForeignKey(User,on_delete=models.CASCADE) 
    ticket = models.ForeignKey(ticket, on_delete=models.CASCADE) 
    text = models.CharField(max_length=500) 
    status = models.CharField(max_length=100) 
    id = models.AutoField(primary_key=True)