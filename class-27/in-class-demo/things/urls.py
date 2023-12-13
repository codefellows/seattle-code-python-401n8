from django.urls import path
from .views import ThingListView, ThingDetailView


urlpatterns = [
    path('', ThingListView.as_view(), name='thing_list'),
    # think of like there is a variable named `pk` which is an integer
    path('<int:pk>/', ThingDetailView.as_view(), name='thing_detail')
]
