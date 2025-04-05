from django.contrib import admin

# Register your models here.
from .models import Farmer, Product, Order

admin.site.register(Farmer)
admin.site.register(Product)
admin.site.register(Order)
