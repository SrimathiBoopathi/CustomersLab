from rest_framework import generics
from .models import Account
from .serializers import AccountSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Account
from .utils import send_data_to_destinations

class AccountListCreateAPIView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


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