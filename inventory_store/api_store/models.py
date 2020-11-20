from django.db import models
from datetime import date
# Create your models here.


class sale_details(models.Model):
    sale_name = models.CharField(max_length=128)
    sale_date = models.DateField()
    price_cuts = models.CharField(max_length=128)

    

class Product(models.Model):
    name = models.CharField(max_length=128)
    year_launched = models.IntegerField()
    manufacturer = models.CharField(max_length=128)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f"{self.name} from -> {self.manufacturer}"


class Batch(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    units = models.IntegerField()
    date_produced = models.DateField()
    expiry_date = models.DateField()
    total = models.IntegerField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'Batch'
        verbose_name_plural = 'Batches'

    def save(self, *args, **kwargs):
        if not self.id:
            self.total = self.units
            super(Batch, self).save(*args, **kwargs)
        else:
            super(Batch, self).save(*args, **kwargs)

    @property
    def freshness(self):
        if (date.today() - self.expiry_date).days > 0:
            return "expired"
        elif (self.expiry_date - date.today()).days <= 3:
            return "expiring today..."
        else:
            return "fresh"

    def __str__(self):
        return f"{self.id} - {self.product}"


class Order(models.Model):
    order_date = models. DateField()
    batch = models.ForeignKey(
        Batch, on_delete=models.CASCADE, related_name="batch_in_order")
    units = models.IntegerField()
    company = models.CharField(max_length=128)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def save(self, *args, **kwargs):
        if not self.id:
            if self.units < self.batch.total:
                self.batch.total -= self.units
                self.batch.save()
                super(Order, self).save(*args, **kwargs)
            else:
                return None

    def __str__(self):
        return f"{self.order_date} - {self.batch}"
