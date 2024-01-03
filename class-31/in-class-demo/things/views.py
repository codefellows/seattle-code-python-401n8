# Instead of using vanilla django views, use DRF views for our API
from rest_framework import generics
from .serializers import ThingSerializer
from .models import Thing


# have a list view
class ThingList(generics.ListCreateAPIView):
    queryset = Thing.objects.all()  # gets all the Things
    serializer_class = ThingSerializer


# have a detail view
class ThingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Thing.objects.all()  # gets all the Things
    serializer_class = ThingSerializer
