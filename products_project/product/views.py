from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Product
from .seriallizer import ProductSerializer

# Create your views here.
def index(request):
    latest_product_list = Product.objects.all()[:5]
    context = {
        'latest_product_list': latest_product_list,
    }
    
    return render(request, 'product/index.html', context)


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    
    return render(request, 'product/detail.html', context)


def image(request, product_id):
    return HttpResponse("You're looking at the image of product "+ str(product_id))


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer