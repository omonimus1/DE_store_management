from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import logout

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def product(request):
    return render(request, 'product.html')

def card(request):
    return render(request, 'layality_card.html')

def offer(request):
    return render(request, 'offers.html')

def finance(request):
    return render(request, 'finance.html')

def logout(request):
    logout(request)

    