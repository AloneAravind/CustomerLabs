from django.urls import path
from . import views

urlpatterns = [
    path('', views.DestinationListCreateView.as_view(), name='destination-list-create'),
    path('<int:pk>/', views.DestinationRetrieveUpdateDestroyView.as_view(), name='destination-detail'),
]

