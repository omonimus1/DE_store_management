# project/project/celery.py

from __future__ import absolute_import

import os
from .models import Product

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

from django.conf import settings 

# app = Celery('proj')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

@app.task(bind=True)
def checkStock(self):
    product_list = Product.objects.all()
    for product in product_list:
        if product.stock < product.minimum_stock:
            if product.stock == 0 and product.available is True:
                Product.set_product_as_not_available(product.id)
            Product.send_email_alert('The product '+ product.name +' (id: '+product.id +' needs to be re-odered')
    print('stock checked')