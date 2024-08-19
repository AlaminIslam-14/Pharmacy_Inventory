from rest_framework import serializers
from .models import Order
from stock.models import Stock
from stock.serializers import StockSerializer
from cart.models import CartItem,Cart
import logging
 
logger = logging.getLogger(__name__)
 
class OrderSerializer(serializers.ModelSerializer):
    updated_stock = serializers.SerializerMethodField()
 
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['total_cost', 'updated_stock']
    
    def __init__(self, *args, **kwargs):
        super(OrderSerializer, self).__init__(*args, **kwargs)
        if self.context['request'].method != 'PUT':
            self.fields['status'].read_only = True
 
    def get_updated_stock(self, obj):
        stocks = Stock.objects.all()
        return StockSerializer(stocks, many=True).data
 
    def create(self, validated_data):
        order = super().create(validated_data)
        logger.info(f"Order created with ID: {order.id}")
        return order
 
    def update_stock(self, order):
        cart_items = CartItem.objects.filter(cart_id=order.cart_id)
        for item in cart_items:
            stock = Stock.objects.get(drug_id=item.drug_id)
            stock.quantity -= item.quantity
            stock.save()
            logger.info(f"Updated stock for drug_id {item.drug_id}: new quantity {stock.quantity}")
        cart_items.delete()
        cart = order.cart_id
        cart.total_cost = 0
        cart.save(update_fields=['total_cost'])
        logger.info(f"Cart {cart.id} total cost set to zero and saved.")
 
            
 
    def update(self, instance, validated_data):
        previous_status = instance.status
        instance = super().update(instance, validated_data)
        if previous_status != 'approved' and instance.status == 'approved':
            logger.info(f"Order {instance.id} status changed to APPROVED. Updating stock.")
            self.update_stock(instance)
        return instance