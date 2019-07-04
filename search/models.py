from django.db import models

# Create your models here.

class Company(models.Model):
    no=models.CharField(max_length=20)
    sym=models.CharField(max_length=20)
    name=models.CharField(max_length=70)

