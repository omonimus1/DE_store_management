from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib import messages
from .models import LoyalCard, Product, User, Offer, Category
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def index(request):
    return render(request, 'index.html')

def create_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

def doLogin(request):
    username= request.GET.get('username')
    password= request.GET.get('password')
    user = authenticate(request, username=username, password=password )
    if user is not None:
        login(request,user)
        messages.info(request, 'welcome')             
        return render(request, 'index.html')

    else:
        messages.info(request, 'something wrong during authentication')
        return render(request, 'login.html')

def loginPage(request):
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
    if request.POST:
        new_offer = Offer()
        new_offer.name = request.POST.get('name')
        new_offer.description = request.POST.get('description')
        new_offer.save()
    offer_list = Offer.objects.all()
    return render(request, 'offers.html', {'offers': offer_list})


def finance(request):
    return render(request, 'finance.html')

def log_user_out(request):
    logout(request)
    return render(request, 'login.html')

