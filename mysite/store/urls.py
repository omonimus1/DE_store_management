from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="teacher"),
    path('login', views.loginPage),
    path('product', views.product),
    path('card', views.card),
    path('offer', views.offer),
    path('finance', views.finance),
    path('logout', views.log_user_out),
    path('updateProductPrice', views.updateProductPrice)
]