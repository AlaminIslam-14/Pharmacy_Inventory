from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['total_cost']
    
    def __init__(self, *args, **kwargs):
        super(OrderSerializer, self).__init__(*args, **kwargs)
        # Make 'status' read-only for all requests except PUT
        if self.context['request'].method != 'PUT':
            self.fields['status'].read_only = True
 