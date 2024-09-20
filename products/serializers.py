from rest_framework import serializers
from .models import Product , Carousel


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class carouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carousel
        fields = '__all__'