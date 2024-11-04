from rest_framework import serializers
from .models import User,Product,Review,Category,Order

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        slug_field='username'
        fields='__all__'