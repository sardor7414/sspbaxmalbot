from rest_framework import serializers
from .models import Appeals


class AppealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appeals
        fields = '__all__'
