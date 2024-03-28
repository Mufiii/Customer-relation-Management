from rest_framework import serializers
from authentication.models import User

class AdminSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    
    class Meta:
        model = User
        fields = ['email','password','confirm_password']
        
    
    def validate(self,data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError("Password does not Match")
        return data


class AdminloginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    
    class Meta:
      model = User
      fields = ['email','password']


