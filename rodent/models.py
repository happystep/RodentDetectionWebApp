from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Rodent(models.Model):
    name = models.CharField(max_length=200)
    age = models.FloatField()
