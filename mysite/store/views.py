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
    breakpoint()
    if request.POST:
        # Product.update_price(request.POST.get('id'), request.POST.get('price'))
        Product.update_price(1, 333)
        breakpoint()

    breakpoint()
    product_list = Product.objects.all()
    messages.info(request, 'Product updated')
    return render(request, 'product.html', {'products': product_list})


def updateProductPrice(request):
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
    return HttpResponse('Log out correctly')

