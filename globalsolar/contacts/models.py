from django.db import models
from datetime import datetime


class Contact(models.Model):
    title = models.CharField(max_length=250)
    work_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    message = models.TextField(blank=True)
    address = models.CharField(max_length=200, blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.name
