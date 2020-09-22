from django.db import models
from datetime import datetime
from django.conf import settings


class Catalog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    catalog_type = models.CharField(max_length=30)
    power = models.CharField(max_length=30)
    price = models.IntegerField()
    made = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    guarantee = models.CharField(max_length=50)
    is_published = models.BooleanField(default=True)
    photo_0 = models.ImageField(upload_to="photos/%Y/%m/%d/")
    photo_1 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_2 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_3 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)

    def __str__(self):
        return self.title
