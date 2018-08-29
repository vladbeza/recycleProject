from decimal import Decimal
from django.conf import settings
from shopRecycle.models import Product
from cupon.models import Cupon

import pdb

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if cart is None:
            self.session[settings.CART_SESSION_ID] = {}
            cart = self.session[settings.CART_SESSION_ID]
        self.cart = cart

        self.cupon_id = self.session.get("cupon_id")

        self.key_price = "price"
        self.key_count = "count"
        self.key_color = "color"
        self.key_total_price = "total_price"
        self.key_product = "product"

    @property
    def cupon(self):
        return Cupon.objects.get(id=self.cupon_id) if self.cupon_id is not None else None

    def get_discount(self):
        if self.cupon is not None:
            return (self.cupon.discount / Decimal(100)) * self.get_total_price()
        return Decimal(0)

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {self.key_count: 0,
                                     self.key_price: product.price}
        if update_quantity:
            self.cart[product_id][self.key_count] = quantity
        else:
            self.cart[product_id][self.key_count] += 1
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        products_ids = self.cart.keys()
        products = Product.objects.filter(id__in=products_ids)
        for product in products:
            self.cart[str(product.id)][self.key_product] = product

        for item in self.cart.values():
            item[self.key_price] = Decimal(item[self.key_price])
            item[self.key_total_price] = item[self.key_price] * item[self.key_count]
            yield item

    def __len__(self):
        return sum([item[self.key_count] for item in self.cart.values()])

    def get_total_price(self):
        return sum([(item[self.key_count] * Decimal(item[self.key_price])) for item in self.cart.values()])

    def get_total_price_after_discount(self):
        return self.get_total_price() - self.get_discount()

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True