from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)
def __str__(self):
    return f'{self.name} {self.price} {self.stock} {self.image_url}'



class Carousel(models.Model):
    carousel_url = models.CharField(max_length=2083)
    def __str__(self):
        return f'{self.carousel_url} '