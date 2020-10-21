from django.db import models

class Delivery(models.Model):
    map_name = models.CharField(max_length=70, blank=False, default='', unique=True)

class Route(models.Model):
    delivery = models.ForeignKey(Delivery, related_name='routes', on_delete=models.CASCADE)
    origin = models.CharField(max_length=70, blank=False, default='')
    destination = models.CharField(max_length=70, blank=False, default='')
    distance = models.IntegerField(default=0)