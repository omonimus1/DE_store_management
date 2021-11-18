from django.test import TestCase

# Create your tests here.
from .models import *
class LoyalCardTestCase(TestCase):
    def setUp(self):
        User.objects.create(name="Davide", username="bob99", email="d@gmail.com", password="cc", level=1, created_at='2021-03-03')
        new_user =  User.objects.get(email="d@gmail.com")
        LoyalCard.objects.create(user=new_user, points=200, active=True)

    def test_card_being_disabled(self):
        user =  User.objects.get(email="d@gmail.com")
        card = LoyalCard.objects.get(user=user)
        LoyalCard.disable_card(card.id)
        card = LoyalCard.objects.get(user=user)
        self.assertEqual(card.active, False)


    def test_card_being_enabled(self):
        user =  User.objects.get(email="d@gmail.com")
        card = LoyalCard.objects.get(user=user)
        LoyalCard.enable_card(card.id)
        card = LoyalCard.objects.get(user=user)
        self.assertEqual(card.active, True)


class ProductTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name='test')
        category = Category.objects.last()
        Offer.objects.create(name='test')
        test_offer = Offer.objects.last()
        Product.objects.create(name="Mac", category=category, offer = test_offer)
        

    def test_update_price_product(self):
        test_product = Product.objects.last()
        Product.update_price(test_product.id, 99.99)
        test_product = Product.objects.last()
        product_price = test_product.price
        self.assertEqual(str(test_product.price), '99.99')

