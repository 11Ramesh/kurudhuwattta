# myapp/serializers.py

from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UseRegister
        fields = '__all__'
