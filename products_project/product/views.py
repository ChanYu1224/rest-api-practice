from django.shortcuts import get_object_or_404, render
from .models import Product
from .seriallizer import ProductSerializer
from rest_framework import generics

# Create your views here.
def index(request):
    latest_product_list = Product.objects.all()[:5]
    context = {
        'latest_product_list': latest_product_list,
    }
    return render(request, 'product/index.html', context)


def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = { 
        'product': product,
    }
    return render(request, 'product/detail.html', context)


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer