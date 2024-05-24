from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Account
from app1.utils import send_data_to_destinations

# Create your views here.
from rest_framework import generics
from .models import Destination
from .serializers import DestinationSerializer

class DestinationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

class DestinationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

@api_view(['POST'])
def incoming_data(request):
    app_secret_token = request.headers.get('CL-X-TOKEN')
    if not app_secret_token:
        return Response({'message': 'Un Authenticate'}, status=401)

    try:
        account = Account.objects.get(app_secret_token=app_secret_token)
    except Account.DoesNotExist:
        return Response({'message': 'Un Authenticate'}, status=401)

    data = request.data
    http_method = request.method

    if http_method == 'GET' and not isinstance(data, dict):
        return Response({'message': 'Invalid Data'}, status=400)

    send_data_to_destinations(account.account_id, data)

    return Response({'message': 'Data received and sent to destinations successfully'})