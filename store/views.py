from django.shortcuts import render

from store.models import Product,Category


def home(request):
    ctg = Category.objects.all()
    product = Product.objects.all()
    ctx={
        'ctg':ctg,
        'product':product,
    }
    return render(request,'index.html',ctx)

def contact(request):
    ctx={}
    return render(request,'contact.html',ctx)

def products(request,slug=None):
    ctg = Category.objects.all()
    product = Product.objects.filter(category__slug=slug) if slug else Product.objects.all()
    ctx={
        'ctg':ctg,
        'product':product,
    }
    return render(request,'products.html',ctx)

def register(request):
    ctx={}
    return render(request,'register.html',ctx)

def single(request):
    ctx={}
    return render(request,'single.html',ctx)
