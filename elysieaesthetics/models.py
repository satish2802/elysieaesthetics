# models.py
from django.db import models

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    service = models.CharField(max_length=100)
