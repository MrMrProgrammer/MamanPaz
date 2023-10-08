from django.urls import path
from . import views

urlpatterns = [
    path('allOrders', views.ShowOrders.as_view())
]
