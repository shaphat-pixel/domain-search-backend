from rest_framework import serializers
from .models import *


class Name_Cheap_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Name_Cheap
        fields = '__all__'



class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = '__all__'


class HoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hover
        fields = '__all__'