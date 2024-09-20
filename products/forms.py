from django import forms
from .models import Product , Carousel

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'stock', 'price', 'image_url']


class CarouselForm(forms.ModelForm):
    class Meta:
        model = Carousel
        fields = ['carousel_url']