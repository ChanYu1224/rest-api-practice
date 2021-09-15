from django.db import models
from django.db import models

class Product(models.Model):
    image = models.ImageField(upload_to='img/products/')
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.IntegerField()

    def __str__(self):
        return self.name
