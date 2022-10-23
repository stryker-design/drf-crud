from pyexpat import model
from rest_framework import serializers
from .models import Item, Location

# Takes django model and turns it into JSON data

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

