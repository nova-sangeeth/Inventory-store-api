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

    def __str__(self):
        return f"{self.id} - {self.product}"

        
class Order(models.Model):
    order_date = models. DateField()
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, related_name="batch_in_order")
    units = models.IntegerField()
    company = models.CharField(max_length = 128)

    def save(self, *args, **kwargs):
        if not self.id:
            if self.units < self.batch.total:
                self.batch.total -= self.units
                self.batch.save()
                super(Order,self).save(*args, **kwargs)
            else:
                return None

    def __str__(self):
        return f"{self.order_date} - {self.batch}"


