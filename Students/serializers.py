from rest_framework import serializers
from .models import Intern

class InternSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Intern
        Fields = '__all__'