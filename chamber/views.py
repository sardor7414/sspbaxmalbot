from django.shortcuts import render
from rest_framework.response import responses
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Appeals
from .serializers import AppealsSerializer

# Create your views here.

class AppealsViewSet(ModelViewSet):
    queryset = Appeals.objects.all()
    serializer_class = AppealsSerializer
