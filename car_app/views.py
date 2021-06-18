from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView
from .models import Car

class Cars:
    def get_cars(self):
        return Car.objects.all()


class CarsList(Cars, ListView):
    model = Car
    template_name = 'car_app/cars_list.html'


class CarsFilter(Cars, ListView):
    template_name = 'car_app/cars_list.html'
    def get_queryset(self):
        queryset = Car.objects.filter(
            Q(name__in=self.request.GET.getlist("name")) |
            Q(year__in=self.request.GET.getlist("year"))
        ).distinct()
        return queryset