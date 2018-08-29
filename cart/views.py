from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shopRecycle.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from cupon.form import CuponForm
import sys

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product, quantity=cd["count"],
                 update_quantity=cd["update"])
    return redirect("cart:cart_detail")


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)
    cart.remove(product)
    return redirect("cart:cart_detail")


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item["update_quantity_form"] = CartAddProductForm(initial={"count": item["count"],
                                                                   "update": True})
    cupon_form = CuponForm()
    return render(request, 'cart/detail.html', {'cart': cart, 'cupon_form': cupon_form})
