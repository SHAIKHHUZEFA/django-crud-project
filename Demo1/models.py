from django.db import models

# Create your models here.
class Product(models.Model):
    pname=models.CharField(max_length=10)
    pprice=models.IntegerField()
    pquantity=models.IntegerField()
