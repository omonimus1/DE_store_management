from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import LoyalCard, Payment, Product, User, Offer, Category
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def index(request):
    if User.is_user_authenticated(request):
        sale_amount_last_week = Payment.get_sales_amount_in_latest_n_days(7)
        sale_amount_last_trimester = Payment.get_sales_amount_in_latest_n_days(90)
        sale_amount_today = Payment.get_sale_amount_current_day()
        sale_amount_current_year = Payment.get_sale_amount_this_year()
        total_number_of_sales = Payment.get_total_number_of_sales_made()
        total_sale_amount = Payment.get_total_amount_of_sales()
        average_sale_amount = Payment.get_average_sale_amount()

        return render(request, 'index.html', {
           'amount_last_week' : sale_amount_last_week, 
           'amount_last_trimester' : sale_amount_last_trimester,
           'amount_today' :sale_amount_today,
           'sale_amount_current_year':sale_amount_current_year,
           'total_number_of_sales':total_number_of_sales,
           'total_sale_amount':total_sale_amount,
           'average_sale_amount' :average_sale_amount
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
    username= request.GET.get('username')
    password= request.GET.get('password')
    user = authenticate(request, username=username, password=password )
    if user is not None:
        login(request,user)
        total_sale = 1;
        items = Payment.objects.all()
        total_price = sum(items.values_list('amount', flat=True))
        return render(request, 'index.html', {
            'total_sale': total_sale, 
            'total_price' : total_price,
        })

    else:
        messages.info(request, 'something wrong during authentication')
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
    if(request.POST.get('offer_id') == 0):
        messages.info(request, 'ciao ')
        return product(request)
    else:
        messages.info(request, 'cao222')
        product_list = Product.objects.filter(offer = request.POST.get('offer_id'))
        number_of_products = product_list.count()
        list_of_offers = Offer.objects.all()
        return render(request, 'product.html', {
            'products': product_list,
            'products_number' : number_of_products,
            'offers': list_of_offers,
        })
    



def updateProductPrice(request):
    if request.POST:
        id = request.POST.get('id')
        price = request.POST.get('price')
        delivery = request.POST.get('deliver_fee')
        minimum_stock = request.POST.get('minimum_stock')
        Product.update_product(id, price, delivery, minimum_stock)

        return product
    else:
        messages.error(request, 'UpdateProduct was not POST')
        return product


def card(request):
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

