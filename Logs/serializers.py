from rest_framework import serializers
from .models import WorkLog

class WorkLogSerializer(serializers.ModelSerializer):
    class Meta:
        Model = WorkLog
        Fields = '__all__'
        
