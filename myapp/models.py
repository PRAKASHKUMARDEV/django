from django.db import models

# Create your models here.

class datas(models.Model):
    name=models.CharField(max_length=50,default=" ")
    number=models.IntegerField(max_length=12,default="")
    email=models.CharField(max_length=50,default=" ")
    location=models.CharField(max_length=50,default=" ")
    time=models.IntegerField(max_length=50,default=" ")