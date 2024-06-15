from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Account
from .serializers import AccountSerializer
from destinations.models import Destination
from destinations.serializers import DestinationSerializer

class AccountListCreateView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountDestinationsListView(APIView):
    def get(self, request, pk, format=None):
        try:
            account = Account.objects.get(pk=pk)
            destinations = Destination.objects.filter(account=account)
            serializer = DestinationSerializer(destinations, many=True)
            return Response(serializer.data)
        except Account.DoesNotExist:
            return Response({'detail': 'Account not found.'}, status=status.HTTP_404_NOT_FOUND)


# from rest_framework import generics
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status
# from .models import Account
# from .serializers import AccountSerializer
# from destinations.models import Destination
# from destinations.serializers import DestinationSerializer

# # List and Create Account
# class AccountListCreateView(generics.ListCreateAPIView):
#     queryset = Account.objects.all()
#     serializer_class = AccountSerializer

# # Retrieve, Update, and Delete Account
# class AccountRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Account.objects.all()
#     serializer_class = AccountSerializer

# # List all destinations for a specific account
# @api_view(['GET'])
# def list_destinations_for_account(request, pk):
#     try:
#         account = Account.objects.get(pk=pk)
#     except Account.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     destinations = Destination.objects.filter(account=account)
#     serializer = DestinationSerializer(destinations, many=True)
#     return Response(serializer.data)
