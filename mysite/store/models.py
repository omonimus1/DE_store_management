from django.db import models
from django.utils import timezone


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200, blank=False)
    surname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, blank=False)
    password = models.CharField(max_length=200, blank=False)
    level = models.IntegerField(blank=False)
    address = models.CharField(max_length=255, blank=True)
    postcode = models.CharField(max_length=10, blank=True)
    created_at = models.DateField(null=True,  default=timezone.now())
    updated_at = models.DateField(null=True,  default=timezone.now())
    deleted_at = models.DateField(null=True,  default=timezone.now())

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255, blank=False)
    created_at = models.DateField(null=True, default=timezone.now())
    updated_at = models.DateField(null=True, default=timezone.now())
    deleted_at = models.DateField(null=True,  default=timezone.now())
    
    def __str__(self):
        return self.name

class Offer(models.Model):
    name = models.CharField(max_length=255, blank=False, default='')
    description = models.TextField(blank=True)
    created_at = models.DateField(null=True, default=timezone.now())
    updated_at = models.DateField(null=True, default=timezone.now())
    deleted_at = models.DateField(null=True,  default=timezone.now())


    def __str__(self):
            return self.name
class Product(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=False)
    average_rating = models.DecimalField(max_digits=9, decimal_places=1, default=0.0)
    price = models.DecimalField(max_digits=9, decimal_places=2, blank=False)
    available = models.BooleanField(default=True, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    stock_available = models.BooleanField(blank=False, default=True)
    created_at = models.DateField(null=True, default=timezone.now())
    updated_at = models.DateField(null=True, default=timezone.now())
    deleted_at = models.DateField(null=True,  default=timezone.now())


    def __str__(self):
        return self.name

class LoyalCard(models.Model):
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField(blank=False, default=0)
    active = models.BooleanField(blank=False, default=True)
    created_at = models.DateField(null=True, default=timezone.now())
    updated_at = models.DateField(null=True, default=timezone.now())
    deleted_at = models.DateField(null=True,  default=timezone.now())

    def __str__(self):
        return self.name

class Review(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    evaluation = models.DecimalField(max_digits=9, decimal_places=2, blank=True)
    product =  models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(null=True, default=timezone.now())
    updated_at = models.DateField(null=True, default=timezone.now())
    deleted_at = models.DateField(null=True,  default=timezone.now())
