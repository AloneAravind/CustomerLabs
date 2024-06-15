# Update urls.py to include the correct path
from django.urls import path
from .views import IncomingDataView

urlpatterns = [
    path('incoming_data/', IncomingDataView.as_view(), name='incoming_data'),
]
