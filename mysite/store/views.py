from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def product(request):
    return render(request, 'product.html')