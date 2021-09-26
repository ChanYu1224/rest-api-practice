from django.shortcuts import get_object_or_404, render
from .models import Product
from .seriallizer import ProductSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

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


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, format=None):
        return Response({
            'success':'success', 
            'message':'success'
            })
    
    def post(self, request):
        if self.serializer_class.is_valid():
            return Response({
                'success':'success', 
                'message':'success'
                })
        else:
            return Response({
                'success':'failure',
                'message':'bad request'
            })
    
    def put(self, request, pk=None):
        return Response({
            'success':'success', 
            'message':'success'
        })

    def delete(self, request, pk=None):
        return Response({
            'success':'success', 
            'message':'success'
        })