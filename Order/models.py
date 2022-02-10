from django.db import models

# Create your models here.
# --------------------------------------------------------------------------------------
from account.models import CustomerUser
from products.models import Product


class Basket(models.Model):
    customer = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='products', on_delete=models.CASCADE)
    Number_of_products_needed = models.IntegerField()

    @property
    def get_price(self):
        return self.product.price

    get_price.fget.short_description = 'price'


# --------------------------------------------------------------------------------------
class Payment(models.Model):
    basket = models.ManyToManyField(Basket)
    customer = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    order_end_date = models.DateTimeField(blank=True, null=True)
    No_products_in_the_order = models.IntegerField()
    tracking = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    payment_amount = models.DecimalField(max_digits=7, decimal_places=2)


    @property
    def get_products(self):
        return ",".join([p.product.name for p in self.basket.all()])

    get_products.fget.short_description = 'product list'


class SilpImage(models.Model):
    slip = models.ImageField(blank=True, null=True, upload_to='slip/')
    proofoftransfer = models.ImageField(blank=True, null=True, upload_to='หลักฐานการโอนเงิน/')
    payment = models.OneToOneField(Payment,related_name='paymentimage', on_delete=models.CASCADE)
