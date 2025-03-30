from django.urls import path
from .views import ProductListCreateView, OrderCreateView
from paypal.standard.ipn.views import ipn

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list'),
    path('orders/', OrderCreateView.as_view(), name='order-create'),
]
urlpatterns += [
    path('paypal/', ipn, name='paypal-ipn'),
]
