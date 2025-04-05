from rest_framework import serializers
from .models import Product, Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def validate_quantity(self, value):
        
        # Ensure that the quantity is greater than or equal to 1.
        
        if value < 1:
            raise serializers.ValidationError("Quantity must be at least 1.")
        return value

    def validate(self, data):
        
        # Check that the product and user exist before saving the order.
        
        user = data.get("user")
        product = data.get("product")

        if not user:
            raise serializers.ValidationError({"user": "This field is required."})
        if not product:
            raise serializers.ValidationError({"product": "This field is required."})

        # we can add more checks, like checking if the product exists in the database
        if not Product.objects.filter(id=product.id).exists():
            raise serializers.ValidationError({"product": "Product does not exist."})

        return data
