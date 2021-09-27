from django.db.models import fields
from rest_framework import serializers
from .models import*

class registersearilizer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ('username','password','first_name','last_name')
        
class loginserializer(serializers.Serializer):        
   email=serializers.EmailField(max_length=None, min_length=None, allow_blank=False)
   password=serializers.CharField(max_length=34,allow_blank=False)