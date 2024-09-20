from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet , product_list, product_detail , create_product, homeindex , carouselViewSet


router = DefaultRouter()
# router.register(r'products', ProductViewSet)
router.register(r'carousel', carouselViewSet)






urlpatterns = [
    path('', homeindex, name='Home'),
    path('api/', include(router.urls)),
    path('all/', product_list, name='product_list'),
    path('products/<int:id>/', product_detail, name='product_detail'),
    path('create/', create_product, name='create_product'),
  
]
