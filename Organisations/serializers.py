from rest_framework import serializers
from .models import Organisation

class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        Model = 'Organisation'
        Fields = '__all__'