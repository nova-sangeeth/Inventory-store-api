from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length = 128)
    year_launched = models.IntegerField()
    manufacturer = models.CharField(max_length = 128)

    def __str__(self):
        return self.name


