from django.urls import path
from .views import ThingListView, ThingDetailView, ThingCreateView, ThingDeleteView, ThingUpdateView


urlpatterns = [
    path('', ThingListView.as_view(), name='thing_list'),
    # does require the trailing slash
    path('<int:pk>/', ThingDetailView.as_view(), name='thing_detail'),
    path('create', ThingCreateView.as_view(), name='thing_create'),
    path('<int:pk>/delete', ThingDeleteView.as_view(), name='thing_delete'),
    path('<int:pk>/update', ThingUpdateView.as_view(), name='thing_update'),
]
