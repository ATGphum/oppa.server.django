from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=60)
    imageUrl = models.CharField(max_length=120)
    miscimageUrl = models.CharField(max_length=120)
    price = models.FloatField(default=0.0)
    stock = models.PositiveIntegerField(default=1)
    description = models.CharField(max_length=400)
    branddescription = models.CharField(max_length=200)

    def __str__(self):
        return self.title