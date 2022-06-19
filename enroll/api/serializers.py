from dataclasses import field
from enroll.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['id', 'name' , 'email','password']