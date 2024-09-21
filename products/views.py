from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404 , redirect
from .models import Product , Carousel
from .serializers import ProductSerializer , carouselSerializer
from .forms import ProductForm , CarouselForm

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class carouselViewSet(viewsets.ModelViewSet):
    
    queryset = Carousel.objects.all()
    serializer_class = carouselSerializer

def product_list(self, request):

    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})


def homeindex(request):
    carousel = Carousel.objects.all()
    products1 = Product.objects.all()
    return render(request, 'products/index.html', {'carousel': carousel, 'products': products1})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'products/product_detail.html', {'product': product})

def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    
    return render(request, 'products/create_product.html', {'form': form})




  
  