from django.db import models
from shop.models import Product
import datetime
import uuid

# Order Model
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default='')
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    date = models.DateField(default=datetime.datetime.today)
    customer = models.CharField(max_length=25, null=False)
    customer_id = models.UUIDField(default=uuid.uuid1, editable=True, null=False)
    address = models.CharField(max_length=70, default='', null=False)
    city = models.CharField(max_length=25, default='', null=False)
    state = models.CharField(max_length=25, default='', null=False)
    pin = models.CharField(max_length=6, default='', null=False)
    phone = models.CharField(max_length=10, default='', null=False)
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(f'{self.order_id} - order({self.customer_id})')

    def place_order(self):
        self.save()

    @staticmethod
    def get_order_by_customer(customer):
        return Order.objects.filter(customer=customer).order_by('date').reverse()