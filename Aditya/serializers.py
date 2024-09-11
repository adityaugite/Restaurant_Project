from rest_framework import serializers
from .models import OrderNow, FoodItem

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = '__all__'

class OrderNowSerializer(serializers.ModelSerializer):
    food_items = FoodItemSerializer(many=True, read_only=True)

    class Meta:
        model = OrderNow
        fields = '__all__'
