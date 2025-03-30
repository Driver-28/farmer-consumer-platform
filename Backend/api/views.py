from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer
from django.core.mail import send_mail
from django.conf import settings

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
def send_order_confirmation(user_email):
    send_mail(
        'Order Confirmation',
        'Thank you for your order! We will process it soon.',
        settings.EMAIL_HOST_USER,
        [user_email],
        fail_silently=False,
    )
