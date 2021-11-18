from django.db import models
from django.utils import timezone
from django.conf import settings
from django.db.models.signals import post_save
from django.db import models
from django.db.models import Sum
from django.shortcuts import reverse
from django.core.mail import send_mail
from django.contrib.auth.models import Group, User
from datetime import datetime, timedelta, datetime


class User(models.Model):
    name = models.CharField(max_length=200, blank=False)
    surname = models.CharField(max_length=200)
    username = models.CharField(max_length=255, default=None)
    email = models.EmailField(max_length=200, blank=False)
    password = models.CharField(max_length=200, blank=False)
    level = models.IntegerField(blank=False, default=1)
    created_at = models.DateField(blank=False,  default=timezone.now())
    updated_at = models.DateField(blank=False,  default=timezone.now())
    deleted_at = models.DateField(blank=True, null=True, default=None)

    
    def __str__(self):
        return self.name
    
    def is_user_authenticated(request):
        return request.user.is_authenticated


    def is_user_manager(request):
        user = request.user
        return User.is_user_authenticated(request) and user.groups.filter(name='manager').exists()




class Category(models.Model):
    name = models.CharField(max_length=255, blank=False)
    created_at = models.DateField(null=True, default=timezone.now())
    updated_at = models.DateField(null=True, default=timezone.now())
    deleted_at = models.DateField(blank=True, null=True, default=None)

    def __str__(self):
        return self.name

class Shop(models.Model):
    address = models.CharField(max_length=255, blank=True)
    postcode = models.CharField(max_length=10, blank=True)
    phone = models.CharField(max_length=14, blank=True)
    manager = models.ForeignKey(User, on_delete=models.CASCADE)
    assistance_email = models.EmailField(null=True)
    created_at = models.DateField(null=True, default=timezone.now())
    updated_at = models.DateField(null=True, default=timezone.now())
    deleted_at = models.DateField(blank=True, null=True, default=None)


    def __str__(self):
        return self.name  

class Offer(models.Model):
    name = models.CharField(max_length=255, blank=False, default='Unknown offer')
    description = models.TextField(blank=False, default='Unknown description')
    created_at = models.DateField(null=True, default=timezone.now())
    updated_at = models.DateField(null=True, default=timezone.now())
    deleted_at = models.DateField(blank=True, null=True, default=None)

    def __str__(self):
            return self.name
            
            
class Product(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=False)
    delivery_fee = models.FloatField(blank=False, default=0.0)
    average_rating = models.DecimalField(max_digits=9, decimal_places=1, default=0.0)
    price = models.DecimalField(max_digits=9, decimal_places=2, blank=False)
    available = models.BooleanField(default=True, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    minimum_stock = models.IntegerField(blank=False, default=10)
    stock = models.IntegerField(blank=False, default=0)
    created_at = models.DateField(null=True, default=timezone.now())
    updated_at = models.DateField(null=True, default=timezone.now())
    deleted_at = models.DateField(blank=True, null=True, default=None)

    def __str__(self):
        return self.name

    @staticmethod
    def get_active():
        return Product.objects.filter(available=True)

    def update_product(id, price, delivery, min_stock):
        Product.objects.filter(id = id).update(price = price,minimum_stock=min_stock, delivery_fee=delivery )


    def get_total_number_of_products():
        return Product.objects.count()

    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("core:remove-from-cart", kwargs={
            'slug': self.slug
        })

    def send_email_alert(alert_message):
        send_mail(
            'Product stock alert',
            alert_message, 
            'stock@ed.com',
            ['davidepollicino2015@gmail.com'],
            fail_silently=False,
        )

    def set_product_as_not_available(product_id):
        product = Product.objects.filter(id = id)
        product.available = False

class ProductImage(models.Model):
    product_id = models.ForeignKey(Product,  on_delete=models.CASCADE)
    url = models.URLField(blank=False)
    created_at = models.DateField(null=True, default=timezone.now())
    updated_at = models.DateField(null=True, default=timezone.now())
    deleted_at = models.DateField(blank=True, null=True, default=None)

    def __str__(self):
        return self.name

    
class LoyalCard(models.Model):
    name = models.CharField(max_length=200, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField(blank=False, default=0)
    active = models.BooleanField(blank=False, default=True)
    created_at = models.DateField(null=True, default=timezone.now())
    updated_at = models.DateField(null=True, default=timezone.now())
    deleted_at = models.DateField(blank=True, null=True, default=None)

    def __str__(self):
        return self.name

    def disable_card(request):
        LoyalCard.objects.filter(id=request.id).update(active=False)

    def enable_card(request):
        LoyalCard.objects.filter(id=request.id).update(active=True)

class Review(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    evaluation = models.DecimalField(max_digits=9, decimal_places=2, blank=True)
    product =  models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(null=True, default=timezone.now())
    updated_at = models.DateField(null=True, default=timezone.now())
    deleted_at = models.DateField(blank=True, null=True, default=None)

    def __str__(self):
        return self.name


class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.FloatField()
    created_at = models.DateField(null=True, default=timezone.now())
    updated_at = models.DateField(null=True, default=timezone.now())
    deleted_at = models.DateField(blank=True, null=True, default=None)

    def __str__(self):
        return self.code


class Orderproduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

    def get_total_product_price(self):
        return self.quantity * self.product.price

    def get_total_discount_product_price(self):
        return self.quantity * self.product.discount_price

    def get_amount_saved(self):
        return self.get_total_product_price() - self.get_total_discount_product_price()

    def get_final_price(self):
        if self.product.discount_price:
            return self.get_total_discount_product_price()
        return self.get_total_product_price()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    products = models.ManyToManyField(Orderproduct)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey(
        'Address', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
    billing_address = models.ForeignKey(
        'Address', related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey(
        'Payment', on_delete=models.SET_NULL, blank=True, null=True)
    coupon = models.ForeignKey(
        'Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)
    created_at = models.DateField(null=True, default=timezone.now())
    updated_at = models.DateField(null=True, default=timezone.now())
    deleted_at = models.DateField(blank=True, null=True, default=None)


    def __str__(self):
        return f"{self.billing_address.street_address} of {self.billing_address.apartment_number}"

    def get_total(self):
        total = 0
        for order_product in self.products.all():
            total += order_product.get_final_price()
        if self.coupon:
            total -= self.coupon.amount
        return total

class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(default=timezone.now())
    created_at = models.DateField(null=True, default=timezone.now())
    updated_at = models.DateField(null=True, default=timezone.now())
    deleted_at = models.DateField(blank=True, null=True, default=None)
    
    def __str__(self):
        return self.user.username


    def get_sale_amount_current_day():
        day = datetime.now().day
        year = datetime.now().year
        month = datetime.now().month
        payment_this_year = Payment.objects.filter(created_at__day = day, created_at__year = year, created_at__month = month)
        if payment_this_year.count() == 0:
            return 0.00
        return sum(payment_this_year.values_list('amount', flat=True))

    def get_sale_amount_this_year():
        year = datetime.now().year
        payment_this_year = Payment.objects.filter(created_at__year=year)
        if payment_this_year.count() == 0:
            return 0.00
        return sum(payment_this_year.values_list('amount', flat=True))

    def get_all_sales():
        return Payment.objects.all()

    def get_total_number_of_sales_made():
        return Payment.get_all_sales().count()


    def get_total_amount_of_sales():
        sales = Payment.objects.all()
        if sales.count() == 0:
            return 0.00
        return sum(sales.values_list('amount', flat=True))


    def get_average_sale_amount():
        sales = Payment.objects.all()
        number_of_sales = sales.count()
        total_sales_amount = sum(sales.values_list('amount', flat=True))
        if total_sales_amount == 0.00:
            return 0.00
        return total_sales_amount/number_of_sales


    def get_sale_amount_this_month():
        year = datetime.now().year
        month = datetime.now().month
        payment_this_year = Payment.objects.filter(created_at__year=year, created_at__month=month)
        if payment_this_year.count() == 0:
            return 0.00
        return sum(payment_this_year.values_list('amount', flat=True))


class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_number = models.CharField(max_length=100, blank=True, default='')
    country =  models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    default = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.street_address} of {self.apartment_number}"

    class Meta:
        verbose_name_plural = 'Addresses'
