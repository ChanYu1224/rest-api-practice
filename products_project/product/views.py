from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import context, loader
from .models import Product

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