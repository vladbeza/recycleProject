from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from news.models import NewPost


def main(request):
    main_products = Product.objects.filter(should_be_on_main=True)
    blogs = NewPost.objects.all().order_by("pub_date")[:2]
    categories = Category.objects.all()
    return render(request,'recycleShop/main.html', {"main_products": main_products, "blogs": blogs, "categories": categories})

def product_list(request, category_name=None):
    if category_name is None:
        all_products = Product.objects.all()
        category = None
    else:
        category = get_object_or_404(Category, category_name=category_name)
        all_products = category.products.all()
    categories = Category.objects.all()
    return render(request, 'recycleShop/products.html', {
        'category': category,
        'categories': categories,
        'all_products': all_products
    })


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart_product_form = CartAddProductForm()
    return render(request, 'recycleShop/detail.html',
                             {'product': product,
                              'cart_product_form': cart_product_form})
