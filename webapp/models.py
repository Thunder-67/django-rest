from django.db import models
from django.db.models import Model

# Create your models here.
class categories(models.Model):
    strcategory=models.CharField(max_length=30)
    strcategorythumb=models.URLField(max_length=100)
    strcategorydescribtion=models.TextField()

    def __str__(self):
        return self.strcategory

class meals(models.Model):
    strmeal=models.CharField(max_length=100)
    strmealthumb=models.URLField(max_length=100)
    idmeal=models.IntegerField()

    def __str__(self):
        return self.strmeal
