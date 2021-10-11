from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib import messages
from .models import LoyalCard, Product, User, Offer, Category
from django.contrib.auth import authenticate

def index(request):
    return render(request, 'index.html')

def loginPage(request):
    if request.POST:
        check_if_user_exists = User.objects.filter(name=request.POST.get('email')).exists()
        if check_if_user_exists:
            user = authenticate(request, email=request.POST.get('email'), password=request.POST.get('password'))

            if user is not None:
                login(request,user=user);             
                return HttpResponse('<H1>Logged in!</H1>', status=200)
            else:
                return loginPage

        return loginPage

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

