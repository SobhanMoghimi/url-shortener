from django.db import models


# Create your models here.

class UrlEntity(models.Model):
    long_url = models.CharField(max_length=64, blank=False)
    short_url = models.CharField(max_length=8, blank=False)
