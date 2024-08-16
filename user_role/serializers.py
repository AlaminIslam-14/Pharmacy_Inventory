from rest_framework import serializers
from .models import UserRole
 
class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = '__all__'
 
    def validate(self, data):
        acc_id = data.get('acc_id')
        role = data.get('role')
 
        # Updating UserRole
        if self.instance:
            if self.instance.role != role:
                # Check if another role is already assigned to this account
                if UserRole.objects.filter(acc_id=acc_id).exclude(id=self.instance.id).exists():
                    raise serializers.ValidationError("This account already has another role assigned.")
        else:
            # Creating a new UserRole
            if UserRole.objects.filter(acc_id=acc_id).exists():
                raise serializers.ValidationError("This account already has a role assigned.")
        
        return data