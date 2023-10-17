from django.urls import path
from . import views

urlpatterns = [
    # path('allOrders', views.ShowOrders.as_view())
    path('add-to-order', views.add_to_order, name='add_to_order'),
    path('calcute-order-count', views.CalculateOrder, name='calcute_order_count'),
    path('show-cart', views.ShowCart, name='Show-Cart'),
    path('order-info', views.order_info, name='order-info'),
    path('remove-per-order/<int:orderDetailId>', views.removePerOrder, name="removePerOrder"),
    path('showMomOrders', views.showMomOrders, name='showMomOrders'),
    path('zarinPal', views.zarinPal, name='zarinPal'),
    path('pay_cart', views.pay_cart, name='pay_cart'),
    path('add-date', views.add_date, name='add-date')
]
