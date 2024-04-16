from django.db import models

class Bill(models.Model):
    name = models.CharField(max_length=30)
    product = models.CharField(max_length=10)
    price = models.IntegerField()
    gst = models.IntegerField()
    purchase_date = models.DateField()

    def __str__(self):
        return self.name
