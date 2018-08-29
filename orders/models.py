from django.db import models
from shopRecycle.models import Product
from cupon.models import Cupon
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField


class Order(models.Model):
    cupon = models.ForeignKey(Cupon, on_delete=models.CASCADE, related_name='orders', null=True, blank=True)
    discount = models.IntegerField(default=0, validators=[MinValueValidator(0),
                                                          MaxValueValidator(100)])
    first_name = models.CharField(verbose_name='First name', max_length=50)
    last_name = models.CharField(verbose_name='Last name', max_length=50)
    email = models.EmailField(verbose_name='Email')
    address = models.CharField(verbose_name='Address', max_length=200)
    city = models.CharField(verbose_name='City', max_length=50)
    phone_number = PhoneNumberField(verbose_name="Phone number", null=True)
    created = models.DateTimeField(verbose_name='Created', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Updated', auto_now=True)
    paid = models.BooleanField(verbose_name='Paid', default=False)

    class Meta:
        ordering = ('-created', )
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return "Order: {}".format(self.id)

    def get_total_price(self):
        total_price = sum([item.total_price() for item in self.items.all()])
        return total_price - total_price * (self.discount / Decimal('100'))


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    price = models.DecimalField(verbose_name='Price', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name='Quantity', default=1)

    def __str__(self):
        return str(self.id)

    def total_price(self):
        return self.price * self.quantity
