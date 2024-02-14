from django.db import models

class Hospital(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField(blank=True)
    capacity = models.IntegerField()
