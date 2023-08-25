from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppealsViewSet

router = DefaultRouter()
router.register('', AppealsViewSet)

urlpatterns = [
    path('', include(router.urls))
]