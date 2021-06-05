from django.db import models

# Create your models here.
class Rice(models.Model):
    temp=models.IntegerField()
    soilmoist=models.IntegerField()
    humidity=models.IntegerField()

class Paddy(models.Model):
    temp=models.IntegerField()
    soilmoist=models.IntegerField()
    humidity=models.IntegerField()
   
