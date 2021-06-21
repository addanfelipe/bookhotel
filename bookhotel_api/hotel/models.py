from typing import Literal
from django.db import models

# Create your models here.


class HotelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def get_cheapest(self, client_type: Literal['Regular', 'Reward'], count_week: int, count_weekend: int):
        if client_type == 'Regular':
            column_week, column_weekend = 'rate_week_regular', 'rate_weekend_regular'
        else:
            column_week, column_weekend = 'rate_week_loyalty', 'rate_weekend_loyalty'

        sql = f'''
SELECT
        hotel_hotel.id,
        hotel_hotel.name
FROM
        hotel_hotel
GROUP BY
        hotel_hotel.id
ORDER BY
        SUM(hotel_hotel.{column_week}) * {count_week} + SUM(hotel_hotel.{column_weekend}) * {count_weekend},
        hotel_hotel.excellence_rating DESC
LIMIT 1
'''
        result = self.raw(sql)
        return result[0]


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    excellence_rating = models.IntegerField()
    rate_week_regular = models.FloatField()
    rate_week_loyalty = models.FloatField()
    rate_weekend_regular = models.FloatField()
    rate_weekend_loyalty = models.FloatField()

    objects = HotelManager()
