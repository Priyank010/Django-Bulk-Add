from rest_framework import serializers
from .models import *

class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = '__all__'
