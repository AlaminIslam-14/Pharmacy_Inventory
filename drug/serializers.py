from rest_framework import serializers
from .models import Drug
from user_role.models import UserRole  

class DrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = '__all__'

    def validate_acc_id(self, value):
        if not UserRole.objects.filter(acc_id=value, role=UserRole.SELLER).exists():
            raise serializers.ValidationError("The account must have the role 'Company' to associate with a drug.")
        return value
