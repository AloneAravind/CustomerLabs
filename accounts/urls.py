from django.urls import path
from . import views

urlpatterns = [
    path('', views.AccountListCreateView.as_view(), name='account-list-create'),
    path('<int:pk>/', views.AccountRetrieveUpdateDestroyView.as_view(), name='account-detail'),
    path('<int:pk>/destinations/', views.AccountDestinationsListView.as_view(), name='account-destinations'),
]
