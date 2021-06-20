from rest_framework.permissions import AllowAny
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class Cheapest(views.APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        params = request.query_params['input']
        return Response({
            "cheapest": "Lakewood"
        })
