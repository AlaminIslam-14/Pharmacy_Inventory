from rest_framework import serializers
from .models import Cart, CartItem

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
        read_only_fields = ['total_cost']

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'
        read_only_fields = ['item_cost']
        
    def validate(self, data):
        drug = data['drug_id']
        quantity = data['quantity']
        data['item_cost'] = drug.price * quantity
        return data
