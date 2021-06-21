from hotel.types import ClientType

from django.db import models
from django.db.models import F

# Create your models here.


class HotelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def get_cheapest(self, client_type: ClientType, count_week: int, count_weekend: int):
        column_week, column_weekend = (
            ('rate_week_regular', 'rate_weekend_regular') if client_type == 'Regular' else
            ('rate_week_loyalty', 'rate_weekend_loyalty')
        )

        result = self.annotate(
            total=(
                F(column_week) * count_week
                + F(column_weekend) * count_weekend
            )
        ).order_by(
            'total',
            '-excellence_rating'
        ).first()

        return result


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    excellence_rating = models.IntegerField()
    rate_week_regular = models.FloatField()
    rate_week_loyalty = models.FloatField()
    rate_weekend_regular = models.FloatField()
    rate_weekend_loyalty = models.FloatField()

    objects = HotelManager()
