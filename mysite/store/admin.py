from django.contrib import admin
from .models import User, Category, Offer, Product, LoyalCard, Review

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Offer)
admin.site.register(Product)
admin.site.register(LoyalCard)
admin.site.register(Review)
# Register your models here.
