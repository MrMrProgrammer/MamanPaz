from django.shortcuts import render
from django.views.generic import ListView

from .models import Cart


# Create your views here.


class ShowOrders(ListView):
    model = Cart
    template_name = 'Order/showOrders.html'
    queryset = Cart.objects.all()
    context_object_name = 'orders'