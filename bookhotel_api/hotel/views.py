from hotel.models import Hotel
from datetime import date, datetime

from rest_framework import views
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

# Create your views here.


class Cheapest(views.APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        input = request.query_params['input']
        [client_type, dates_str] = input.split(': ')
        dates_str = dates_str.split(', ')

        def str_to_date(date_str):
            date_str = date_str[:9]
            return datetime.strptime(date_str, '%d%b%Y').date()

        def count_week_type(dates: date):
            count_week, count_weekend = 0, 0
            for date in dates:
                if date.weekday() in [5, 6]:
                    count_weekend += 1
                else:
                    count_week += 1

            return [count_week, count_weekend]

        dates = [str_to_date(_date_str) for _date_str in dates_str]
        [count_week, count_weekend] = count_week_type(dates)
        
        if client_type == 'Regular':
            column_week, column_weekend = ('rate_week_regular', 'rate_weekend_regular')
        else:
            column_week, column_weekend = ('rate_week_loyalty', 'rate_weekend_loyalty')

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
        result = Hotel.objects.raw(sql)

        return Response({
            "cheapest": result[0].name
        })