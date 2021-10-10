from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib import messages
from .models import Product, User, Offer, Category

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def product(request):
    if request.POST:
        Product.objects.filter(request.GET.get('id')).update(price = request.GET.get('price'))

    product_list = Product.objects.filter.all()
    messages.info(request, 'Product updated')
    return render(request, 'product.html', {'products': product_list})


def updateProductPrice(request):
    return product


def card(request):
    return render(request, 'layality_card.html')

def offer(request):
    return render(request, 'offers.html')

def finance(request):
    return render(request, 'finance.html')

def logout(request):
    logout(request)

