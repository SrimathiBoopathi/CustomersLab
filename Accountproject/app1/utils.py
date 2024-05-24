from .models import Account
from django.core.exceptions import ObjectDoesNotExist

def send_data_to_destinations(account, data):
    try:
        account_obj = Account.objects.get(account_id=account)
    except ObjectDoesNotExist:
        print("Account does not exist.")
        return

    destinations = account_obj.destinations.all()
    for destination in destinations:
        # Send data to destination using destination.url, destination.http_method, and destination.headers
        print(f"Sending data to {destination.url} using {destination.http_method} method with headers {destination.headers}")

