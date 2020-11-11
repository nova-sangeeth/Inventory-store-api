from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length = 128)
    year_launched = models.IntegerField()
    manufacturer = models.CharField(max_length = 128)

    def __str__(self):
        return self.name


class Batch(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    units = models.IntegerField() 
    date_produced = models.DateField()
    expiry_date = models.DateField()
    total = models.IntegerField(blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.total = self.units
            super(Batch, self).save(*args, **kwargs)
        else:
            super(Batch, self).save(*args, **kwargs)

