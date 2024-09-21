# accounts/urls.py

from django.urls import path
from .views import CategoryViewSet
from django.urls import include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'categories', CategoryViewSet)



urlpatterns = [
    path('', include(router.urls)),
]
