import datetime
# import celery
from .models import Product

@celery.decorators.periodic_task(run_every=datetime.timedelta(minutes=60)) # here we assume we want it to be run every 60 mins
def checkStock():
    product_list = Product.objects.all()
    for product in product_list:
        if product.stock < product.minimum_stock:
            if product.stock == 0 and product.available is True:
                Product.set_product_as_not_available(product.id)
            Product.send_email_alert('The product '+ product.name +' (id: '+product.id +' needs to be re-odered')
    print('stock checked')