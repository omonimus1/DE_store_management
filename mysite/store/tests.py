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
