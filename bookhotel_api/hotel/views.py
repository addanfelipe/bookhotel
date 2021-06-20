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

        print(count_week, count_weekend)

        # datetime_object = datetime.strptime('17Mar2009', '%d%b%Y').date()

        # print(datetime_object)

        # print(date(2009, 3, 16).weekday())

        # print(client_type)
        # print(dates)

        return Response({
            "cheapest": "Lakewood"
        })
