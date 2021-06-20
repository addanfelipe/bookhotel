from django.db import models

# Create your models here.


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    excellence_rating = models.IntegerField()
    rate_week_regular = models.FloatField()
    rate_week_loyalty = models.FloatField()
    rate_weekend_regular = models.FloatField()
    rate_weekend_loyalty = models.FloatField()
