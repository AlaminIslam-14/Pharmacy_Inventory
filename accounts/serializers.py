from rest_framework import serializers
from .models import Accounts
 
class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = '__all__'
        
    def validate(self, data):
        license_no = data.get('license_no')
        
        if Accounts.objects.filter(license_no=license_no).exists():
            raise serializers.ValidationError("An account with this license number already exists.")
        
        return data