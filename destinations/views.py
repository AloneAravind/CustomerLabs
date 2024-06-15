
# from rest_framework import generics
# from .models import Destination
# from .serializers import DestinationSerializer

# # List and Create Destination
# class DestinationListCreateView(generics.ListCreateAPIView):
#     queryset = Destination.objects.all()
#     serializer_class = DestinationSerializer

#     def get_queryset(self):
#         account_id = self.request.query_params.get('account_id')
#         if account_id:
#             return self.queryset.filter(account__id=account_id)
#         return self.queryset

# # Retrieve, Update, and Delete Destination
# class DestinationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Destination.objects.all()
#     serializer_class = DestinationSerializer
from rest_framework import generics
from .models import Destination
from .serializers import DestinationSerializer

class DestinationListCreateView(generics.ListCreateAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

class DestinationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
