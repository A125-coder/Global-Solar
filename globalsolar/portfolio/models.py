from django.db import models
from datetime import datetime


class Portfolio(models.Model):
    title = models.CharField(max_length=250)
    product_type = models.CharField(max_length=250, blank=True)
    amount = models.IntegerField(blank=True, null=True)
    voltage = models.IntegerField()
    list_date = models.DateTimeField(default=datetime.now)
    address = models.CharField(max_length=250, blank=True)
    is_published = models.BooleanField(default=True)
    photo_0 = models.ImageField(upload_to="photos/%Y/%m/%d/")

    def __str__(self):
        return self.title
