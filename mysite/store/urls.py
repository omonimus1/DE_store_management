from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('product', views.product),
    path('card', views.card),
    path('offer', views.offer),
]