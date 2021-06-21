from hotel.validators import CheapestGetValidator

from rest_framework import views
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from hotel.models import Hotel

# Create your views here.


class Cheapest(views.APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        _input = request.query_params.get('input', None)
        form = CheapestGetValidator(data={'input': _input})

        if not form.validate():
            return Response(form.errors, 400)

        hotel = Hotel.objects.get_cheapest(
            form.client_type, form.count_week, form.count_weekend
        )

        return Response({
            "cheapest": hotel.name
        })
