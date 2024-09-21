from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from .models import Category
from .serializers import CategorySerializer
from rest_framework.response import Response
from rest_framework import status

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically set the user_id field on creation
        serializer.save(user_id=self.request.user.id)

    def get_queryset(self):
        # Filter categories based on the authenticated user
        return Category.objects.filter(user_id=self.request.user.id)
