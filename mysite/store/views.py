from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import LoyalCard, Payment, Product, User, Offer, Category
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def index(request):
    if User.is_user_authenticated(request):
        sale_amount_today = Payment.get_sale_amount_current_day()
        sale_amount_current_year = Payment.get_sale_amount_this_year()
        total_number_of_sales = Payment.get_total_number_of_sales_made()
        total_sale_amount = Payment.get_total_amount_of_sales()
        average_sale_amount = Payment.get_average_sale_amount()
        sale_this_month = Payment.get_sale_amount_this_month()
        return render(request, 'index.html', {
           # 'amount_last_week' : sale_amount_last_week, 
           # 'amount_last_trimester' : sale_amount_last_trimester,
           'amount_today' :sale_amount_today,
           'sale_amount_current_year':sale_amount_current_year,
           'total_number_of_sales':total_number_of_sales,
           'total_sale_amount':total_sale_amount,
           'average_sale_amount' :average_sale_amount,
           'sale_this_month':sale_this_month
        })
    return loginPage(request)


def create_user(request):
    if User.is_user_authenticated(request):
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
    return loginPage(request)


def doLogin(request):
    username= request.POST.get('username')
    password= request.POST.get('password')
    user = authenticate(request, username=username, password=password )
    if user is not None:
        login(request,user)
        sale_amount_today = Payment.get_sale_amount_current_day()
        sale_amount_current_year = Payment.get_sale_amount_this_year()
        total_number_of_sales = Payment.get_total_number_of_sales_made()
        total_sale_amount = Payment.get_total_amount_of_sales()
        average_sale_amount = Payment.get_average_sale_amount()
        sale_this_month = Payment.get_sale_amount_this_month()
        return render(request, 'index.html', {
           # 'amount_last_week' : sale_amount_last_week, 
           # 'amount_last_trimester' : sale_amount_last_trimester,
           'amount_today' :sale_amount_today,
           'sale_amount_current_year':sale_amount_current_year,
           'total_number_of_sales':total_number_of_sales,
           'total_sale_amount':total_sale_amount,
           'average_sale_amount' :average_sale_amount,
           'sale_this_month':sale_this_month
        })
    else:
        messages.info(request, 'User or password are not correct')
        return render(request, 'login.html')


def loginPage(request):
    return render(request, 'login.html')

def product(request):

    if User.is_user_authenticated(request):
        product_list = Product.objects.all()
        number_of_products = product_list.count()
        list_of_offers = Offer.objects.all()
        return render(request, 'product.html', {
            'products': product_list,
            'products_number' : number_of_products,
            'offers': list_of_offers,
        })
    return loginPage(request)

def filterProductByOffer(request):
    offer_id= request.POST.get('offer_id')
    if(request.POST.get('offer_id') == 0):
        return product(request)
    if not Product.objects.filter(offer = offer_id).exists():
        messages.info(request, 'Offer id does not exists')
    else:
        product_list = Product.objects.filter(offer = offer_id )
        number_of_products = product_list.count()
        list_of_offers = Offer.objects.all()
        return render(request, 'product.html', {
            'products': product_list,
            'products_number' : number_of_products,
            'offers': list_of_offers,
        })
    



def updateProductPrice(request):
    # if request.POST:
    id = request.POST.get('id')
    price = request.POST.get('price')
    Product.update_price(request.POST.get('id'), request.POST.get('price'))
    return redirect('/store/product')


def card(request):
    if request.POST:
        if request.POST.get('status') == "true":
            LoyalCard.disable_card(request.POST.get('card_id'))
        else:
            LoyalCard.enable_card(request.POST.get('card_id'))

    if User.is_user_authenticated(request):
        cards = LoyalCard.objects.all()
        return render(request, 'loyalty_card.html', {'cards': cards})

    return loginPage(request)


def offer(request):
    if User.is_user_authenticated(request):
        if request.POST:
            new_offer = Offer()
            new_offer.name = request.POST.get('name')
            new_offer.description = request.POST.get('description')
            new_offer.save()
        offer_list = Offer.objects.all()
        return render(request, 'offers.html', {'offers': offer_list})
    return loginPage(request)


def finance(request):
    if User.is_user_authenticated(request):
        return render(request, 'finance.html')
    return loginPage(request)


def log_user_out(request):
    logout(request)
    return render(request, 'login.html')

