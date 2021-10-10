from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib import messages
from .models import LoyalCard, Product, User, Offer, Category


def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def product(request):
    product_list = Product.objects.all()
    number_of_products = product_list.count()
    return render(request, 'product.html', {
        'products': product_list,
        'products_number' : number_of_products,
    })


def updateProductPrice(request):
    if request.POST:
        Product.update_price(request.POST.get('id'), request.POST.get('price'))
        return product
    else:
        messages.error(request, 'UpdateProduct was not POST')
        return product

def card(request):
    cards = LoyalCard.objects.all()
    return render(request, 'loyalty_card.html', {'cards': cards})

def offer(request):
    return render(request, 'offers.html')

def finance(request):
    return render(request, 'finance.html')

def log_user_out(request):
    logout(request)
    return render(request, 'login.html')

