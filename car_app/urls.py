from django.urls import path
from .views import *

urlpatterns = [
    path('', CarsList.as_view(), name='car_list'),
    path('filter/', CarsFilter.as_view(), name='filter')
]
