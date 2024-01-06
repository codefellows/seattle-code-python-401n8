from django.urls import path
from .views import ThingList, ThingDetail


urlpatterns = [
    path('', ThingList.as_view()),  # don't need the `name='thing_list'`
    path('<int:pk>/', ThingDetail.as_view()),
]
