from urllib import request
from django.shortcuts import render
from .models import Product

# Create your views here.

def products(request):
    pro=Product.objects.all()
    x={'pro':pro.order_by('-price')}
    # x={'pro':str(pro.count())}
    # x={'pro':pro.exclude(price=10)}
    # x={'pro':pro.filter(price__exact=10)}
    # x={'pro':pro.filter(name__contains='o')}
    # x={'pro':pro.filter(price__in=[10,5])}
    # x={'pro':pro.filter(price__range=(2,10))}


    return render(request,'products.html',x)


def product(request):

    return render(request,'product.html')    
