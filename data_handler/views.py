from django.http import JsonResponse
from django.views import View
from accounts.models import Account
import requests

class IncomingDataView(View):
    def post(self, request):
        token = request.headers.get('CL-X-TOKEN')
        if not token:
            return JsonResponse({"error": "Unauthenticated"}, status=401)
        
        try:
            account = Account.objects.get(app_secret_token=token)
        except Account.DoesNotExist:
            return JsonResponse({"error": "Unauthenticated"}, status=401)
        
        data = request.body
        destinations = account.destinations.all()
        for destination in destinations:
            headers = destination.headers
            headers['Content-Type'] = 'application/json'
            if destination.http_method.lower() == 'post':
                response = requests.post(destination.url, headers=headers, data=data)
            elif destination.http_method.lower() == 'get':
                response = requests.get(destination.url, headers=headers, params=data)
            # Handle other methods if necessary
        
        return JsonResponse({"status": "success", "message": "Data forwarded to destinations"})

# Update urls.py to include the correct path
from django.urls import path
from .views import IncomingDataView

urlpatterns = [
    path('incoming_data/', IncomingDataView.as_view(), name='incoming_data'),
]
