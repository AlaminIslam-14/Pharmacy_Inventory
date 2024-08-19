from rest_framework import serializers
from .models import Stock
from django.core.exceptions import ValidationError
 
class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'
 
    def update(self, instance, validated_data):
        drug = validated_data.get('drug_id')
        batch_id = validated_data.get('batch_id')
        quantity = validated_data.get('quantity')
 
        existing_stock = Stock.objects.filter(drug_id=drug, batch_id=batch_id).first()
 
        quantity = validated_data.get('quantity', instance.quantity)
        if(existing_stock.quantit < quantity):
            raise ValidationError("The new quantity cannot be less than the existing quantity.")
        instance.quantity = existing_stock.quantity + quantity
        instance.save(update_fields=['quantity'])
        return instance
 