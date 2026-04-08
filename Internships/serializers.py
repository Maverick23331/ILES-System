from rest_framework import serializers
from .models import Internship

class InternshipSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Internship
        Field = '__all__'